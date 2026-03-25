import firebase_admin
from firebase_admin import credentials, db

# ফায়ারবেস কনসোল থেকে জেনারেট করা JSON কি ফাইল এখানে দিতে হবে
cred = credentials.Certificate("path/to/your/firebase-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://free-9d3b4-default-rtdb.firebaseio.com'
})

def get_all_users():
    ref = db.reference('users')
    users = ref.get()
    for uid, info in users.items():
        print(f"User: {info.get('username')}, Balance: {info.get('winning')}")

# ইউজার লিস্ট দেখতে চাইলে কল করুন
# get_all_users()