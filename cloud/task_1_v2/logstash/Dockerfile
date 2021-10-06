ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json


# RUN logstash-plugin install logstash-input-jdbc
# RUN rm  logstash-core/lib/jars/*
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.6.jar -o /usr/share/logstash/logstash-core/lib/jars/postgresql-42.2.6.jar
# ADD postgresql-42.2.6.jar logstash-core/lib/jars
# RUN logstash-plugin install logstash-input-jdbc