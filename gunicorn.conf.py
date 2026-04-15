def on_starting(server):
    import os
    os.makedirs('data', exist_ok=True)
    try:
        from database import init_db, seed
        init_db()
        seed()
        print("Base de données prête.")
    except Exception as e:
        print(f"Erreur init DB: {e}")

workers = 2
timeout = 120
