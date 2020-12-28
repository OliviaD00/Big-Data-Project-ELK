FROM sebp/elk
ENV ES_HOME /opt/elasticsearch
WORKDIR ${ES_HOME}
RUN bin/elasticsearch-plugin install --batch ingest-attachment

