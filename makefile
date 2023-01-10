image?=image
app?=app
tag?=tag

env:
	export SECRET_KEY='django-insecure-y^s(e-s_)uk*_kqi2&&yrb^z@nsrx3!dn^p2yg21l5-=8gnwdm' && export ENV='DEV'

build:
	docker build . -t ecommerce:0.0

run:
	docker run --publish 127.0.0.1:8000:8000 ecommerce:0.0

push:
	git push master master