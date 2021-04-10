# flattest
aplicación de una API wrapper para cualquier repositorio de GITHUB

pasos para su intalación en docker

1- clonar o descargar este repositorio

2- ejecutar: docker build --build-arg ARG_DEFAULT_PORT=8000 -t flat .

3- ejecutar: docker build . -t flat

4- ejecutar y poner el token de acceso a un repositorio de git, poner el repositorio y la url del repositorio: docker run  -p 8000:8000 -e TOKEN="poneraquitoken" -e REPO="poner aqui repo" -e URL_GIT='poner aqui url de repo' flat


ejemplo:

docker run  -p 8000:8000 -e TOKEN="6377242c554fdhjgjhg684225e" -e REPO="jazzcsa1991/chelita" -e URL_GIT='https://github.com/jazzcsa1991/chelita.git' flat

5- para configurar frontend favor de ir a https://github.com/jazzcsa1991/flatfrontend.git
