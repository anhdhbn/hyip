FROM selenium/node-chrome-debug
USER root
RUN curl https://i.jpillora.com/chisel! | bash

USER seluser
CMD /opt/bin/entry_point.sh & chisel server