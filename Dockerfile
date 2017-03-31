FROM drewantech/drewantech_common:0.3.2
MAINTAINER Benton Drew <benton.s.drew@drewantech.com>
USER root
RUN rm test_common.py
ADD source/ /usr/lib/python3.5/site-packages/demo_random_matrix_generator
ADD service/ .
ENV FLASK_APP demo_random_matrix_generator_web_service.py
ENTRYPOINT ["python3", "-m", "flask", "run"]
CMD ["--host=0.0.0.0", "--port=80"]
