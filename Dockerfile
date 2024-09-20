FROM ubuntu:latest
LABEL authors="jackeen"

ENTRYPOINT ["top", "-b"]