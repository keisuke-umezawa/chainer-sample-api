import responder


api = responder.API(
    cors=True,
    allowed_hosts=["*"],
    cors_params={
        "allow_origins": "*",
        "allow_methods": "*",
        "allow_headers": "*",
    },
)

if __name__ == "__main":
    api.run(address="0.0.0.0", port=5432)
