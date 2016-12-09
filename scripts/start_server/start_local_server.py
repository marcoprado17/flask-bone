from app_factory import create_app

if __name__ == "__main__":
    from configs import default_app_config
    from configs.instance import instance_app_config

    app = create_app(
        default_app_config=default_app_config,
        instance_app_config=instance_app_config
    )
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
