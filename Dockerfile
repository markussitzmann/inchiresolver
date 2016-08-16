FROM appserver_django_image

USER root

COPY . /home/service/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /home/service/nginx.conf /etc/nginx/sites-enabled/
RUN ln -s /home/service/supervisord.conf /etc/supervisor/conf.d/

RUN CONDA_PY=35 pip install -r /home/service/requirements.txt

RUN if [ -d /home/service/project_template/ ]; then cp -r /home/service/project_template/ /tmp; fi && \
	cp -r /home/service/uwsgi/ /tmp && \
	cp /home/service/Dockerfile /tmp && \
	cp /home/service/requirements.txt /tmp && \
	cp /home/service/service.env /tmp && \
	cp /home/service/service-* /tmp && \
	cp /home/service/django-* /tmp && \
	cp /home/service/docker-compose.yml /tmp && \
	cp /home/service/run.sh /tmp && \
	cp /home/service/supervisord.conf /tmp && \
	cp /home/service/nginx.conf /tmp && \
	cp /home/service/uwsgi_params /tmp

EXPOSE 80
CMD ["/home/service/run.sh"]
