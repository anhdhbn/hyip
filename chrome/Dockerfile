FROM selenium/node-chrome-debug
USER root
RUN curl https://i.jpillora.com/chisel! | bash

USER seluser
ENTRYPOINT '/opt/bin/entry_point.sh & chisel server --reverse'