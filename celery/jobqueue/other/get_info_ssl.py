import ssl
import socket
import OpenSSL
from datetime import datetime
from urllib.parse import urlparse

def get_certificate(domain, port=443, timeout=30):
    context = ssl.create_default_context()
    conn = socket.create_connection((domain, port))
    sock = context.wrap_socket(conn, server_hostname=domain)
    sock.settimeout(timeout)
    try:
        der_cert = sock.getpeercert(True)
    finally:
        sock.close()
    return ssl.DER_cert_to_PEM_cert(der_cert)

def get_ssl_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    if parsed_uri.scheme == "http":
        return {}
    certificate = get_certificate(domain)
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)

    issuer = dict(x509.get_issuer().get_components())[b'CN'].decode("utf-8")
    ev_arr = ["EV RSA",  "EV CA", "Extended Validation"]
    from_date = datetime.strptime(x509.get_notBefore().decode("utf-8") , '%Y%m%d%H%M%SZ').date().strftime("%Y-%m-%d")
    to_date = datetime.strptime(x509.get_notAfter().decode("utf-8"), '%Y%m%d%H%M%SZ').date().strftime("%Y-%m-%d")

    return {
        'ev': any([ev in issuer for ev in ev_arr]), 
        'from_date': from_date,
        'to_date': to_date,
        'description': issuer,
        'domain': domain,
    }

# from urllib.parse import urlparse
# from collections import namedtuple

# from OpenSSL import SSL
# from cryptography import x509
# from cryptography.x509.oid import NameOID
# import idna

# from socket import socket


# HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')

# def get_sock_ssl(hostname_idna, sock):
#     ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
#     ctx.check_hostname = False
#     ctx.verify_mode = SSL.VERIFY_NONE

#     sock_ssl = SSL.Connection(ctx, sock)
#     sock_ssl.set_connect_state()
#     sock_ssl.set_tlsext_host_name(hostname_idna)
#     sock_ssl.do_handshake()
#     return sock_ssl

# def get_sock_tls(hostname_idna, sock):
#     ctx = SSL.Context(SSL.TLSv1_METHOD) # most compatible
#     ctx.check_hostname = False
#     ctx.verify_mode = SSL.VERIFY_NONE

#     sock_ssl = SSL.Connection(ctx, sock)
#     sock_ssl.set_connect_state()
#     sock_ssl.set_tlsext_host_name(hostname_idna)
#     sock_ssl.do_handshake()
#     return sock_ssl


# def get_certificate(hostname, port):
#     hostname_idna = idna.encode(hostname)
#     sock = socket()

#     sock.connect((hostname, port))
#     peername = sock.getpeername()

#     sock_ssl = None
#     try:
#         sock_ssl = get_sock_ssl(hostname_idna, sock)
#     except Exception e:
#         print(hostname)
#         raise(e)


#     cert = sock_ssl.get_peer_certificate()
#     crypto_cert = cert.to_cryptography()
#     sock_ssl.close()
#     sock.close()

#     return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)

# def get_alt_names(cert):
#     try:
#         ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
#         return ext.value.get_values_for_type(x509.DNSName)
#     except x509.ExtensionNotFound:
#         return None

# def get_common_name(cert):
#     try:
#         names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
#         return names[0].value
#     except x509.ExtensionNotFound:
#         return None

# def get_issuer(cert):
#     try:
#         names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
#         return names[0].value
#     except x509.ExtensionNotFound:
#         return None

# def get_ssl_info_from_domain(url):
#     parsed_uri = urlparse(url)
#     domain = parsed_uri.netloc
#     port = 443 if parsed_uri.scheme == "https" else 80
#     hostinfo = get_certificate(domain, port)

#     # GeoTrust EV RSA CA 2018
#     # CloudFlare Inc ECC CA-2
#     # Sectigo RSA Extended Validation Secure Server CA
#     # Thawte EV RSA CA 2018
#     # GoGetSSL RSA EV CA
#     # DigiCert SHA2 Extended Validation Server CA

#     ev_arr = ["EV RSA",  "EV CA", "Extended Validation"]
#     issuer = get_issuer(hostinfo.cert)

#     return {
#         'ev': any([ev in issuer for ev in ev_arr]), 
#         'from_date': hostinfo.cert.not_valid_before.strftime('%Y-%m-%d'), 
#         'to_date': hostinfo.cert.not_valid_after.strftime('%Y-%m-%d'), 
#         'description': issuer
#     }


# def get_ssl_info_from_domain(url):
#     parsed_uri = urlparse(url)
#     domain = parsed_uri.netloc
#     requests.get("https://www.ssllabs.com/ssltest/analyze.html?viaform=off&d={}".format(domain))
#     html2 = ""
#     url_ = "https://www.ssllabs.com/ssltest/analyze.html?d={}&latest".format(domain)
#     use_ip_url = False

#     while True:
#         if not use_ip_url:
#             html2 = html.unescape(html2)
#             check  =  re.findall('(analyze\.html.*?)"',  html2)
#             if  len(check) > 1:
#                 url_ = "https://www.ssllabs.com/ssltest/" + check[1]
#                 use_ip_url = True
#         html2 = requests.get(url_).text
#         if "Server Key and Certificate" in html2:
#             break
        
#         time.sleep(1)
#     matches = re.findall('tableCell">.*,(.*)UTC.*<', html2)
#     from_date = str2date_length(matches[0].strip())
#     to_date = str2date_length(matches[1].strip())
#     match = re.findall(r'Extended Validation</(.*?)>', html2)[0]
#     ev = True if match == "font" else False
#     Issuer = re.findall(r'Issuer.*?title=".*?">(.*?)<', html2, re.DOTALL)[0].strip()
#     description = html.unescape(Issuer)
#     return {
#         'ev': ev, 
#         'from_date': from_date.strftime('%Y-%m-%d'), 
#         'to_date': to_date.strftime('%Y-%m-%d'), 
#         'description': description
#     }