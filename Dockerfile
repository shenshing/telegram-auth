FROM archlinux
WORKDIR /koompi-play-telegram
RUN pacman -Syu --noconfirm
RUN pacman -S python3 python-pip cmake gcc python-virtualenv python-distlib linux-headers --noconfirm
COPY requirement.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

