import csv

from app.database import SessionLocal
from app.models import Bank, Branch


def load_data():
    db = SessionLocal()

    bank_cache = {}

    with open("data/bank_branches.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            bank_name = row["bank_name"].strip()

            # Create bank if not exists
            if bank_name not in bank_cache:
                bank = Bank(name=bank_name)
                db.add(bank)
                db.commit()
                db.refresh(bank)
                bank_cache[bank_name] = bank
            else:
                bank = bank_cache[bank_name]

            # Create branch
            branch = Branch(
                ifsc=row["ifsc"].strip(),
                branch=row["branch"].strip(),
                address=row.get("address"),
                bank_id=bank.id,
            )

            db.add(branch)

        db.commit()
        db.close()


if __name__ == "__main__":
    load_data()
    print("Data loaded successfully")
