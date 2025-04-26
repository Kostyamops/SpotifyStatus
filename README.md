# Настройка

Вся настройка бота происходит в [config.py](bot/config.py)

# Управление приложением

### Первоначальный запуск (deploy) приложения в контейнере

```shell
./scripts/docker_deploy.sh
```

### Остановка контейнера, и удаление образа

```shell
./scripts/docker_delete.sh
```

### Остановка контейнера 

```shell
./scripts/docker_stop.sh
```

### Запуск (уже созданного с помощью deploy) образа

```shell
./scripts/docker_start.sh
```

