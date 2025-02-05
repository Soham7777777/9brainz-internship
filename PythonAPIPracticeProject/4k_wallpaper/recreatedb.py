import os
import shutil
import subprocess
from wallpaperzzz import settings


DB_FILE = str(settings.DATABASES["default"]["NAME"]) 
APPS = [app for app in settings.INSTALLED_APPS if app.find(".") == -1 and app.endswith("app")]
MEDIA_ROOT = settings.MEDIA_ROOT


def remove_pycache_dirs(directory: str = ".") -> None:
    """Recursively remove all __pycache__ directories from the given directory."""
    for root, dirs, _ in os.walk(directory):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)


def delete_database() -> None:
    """Remove the SQLite database file."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"✅ Deleted {DB_FILE}")
    else:
        print(f"⚠️ {DB_FILE} not found, skipping.")


def clean_migrations() -> None:
    """Remove all migration files except __init__.py."""
    for app in APPS:
        migrations_path = os.path.join(app, "migrations")
        if os.path.exists(migrations_path):
            for file in os.listdir(migrations_path):
                file_path = os.path.join(migrations_path, file)
                if file != "__init__.py":
                    os.remove(file_path)
            print(f"✅ Cleared migrations for {app}, kept __init__.py")
        else:
            print(f"⚠️ Migrations folder not found for {app}, skipping.")


def run_manage_py(command: str) -> None:
    """Run a Django management command."""
    subprocess.run(["python3", "manage.py", command], check=True)


def mock_database() -> None:
    """Mock the database with test data."""
    subprocess.run(['python3', 'mock.py'], text=True)


def delete_mediaroot() -> None:
    """Delete media root directory."""
    if os.path.isdir(MEDIA_ROOT):
        shutil.rmtree(MEDIA_ROOT)


def main() -> None:
    remove_pycache_dirs()

    print("🚀 Resetting database and migrations...")
    delete_database()
    clean_migrations()

    print("🔄 Running Django migrations...")
    try:
        run_manage_py("makemigrations")
        run_manage_py("migrate")
        print("✅ Database recreated successfully!")
        delete_mediaroot()
        print("✅ Deleted mediaroot successfully!")
        mock_database()
        print("✅ Database mocked successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Django commands: {e}")

    remove_pycache_dirs()


if __name__ == "__main__":
    main()
