#python manage.py shell

from django.contrib.auth.hashers import make_password
for i in range(5):
    print(make_password('senha123'))

# pbkdf2_sha256$870000$1nJO38HbLBUzHl7Pl2Xdtd$mujKG64e2j4Vv2P0VVE7ATlR8O+SjUNquqn81AcPrqo=
# pbkdf2_sha256$870000$miLxkc0BMbLrgl5sS1l0e9$tRtoouyTLiJOZokYWKrv9j7PVwKtwmmIGNweA+hAc+w=
# pbkdf2_sha256$870000$VNgUntFkJiV4HoHGZC1RaI$dSpUliL5KFJ8Lt/iQM4fJqY/rPZg18i59MqZsDgB8Us=
# pbkdf2_sha256$870000$nEvhevKUTehn1Bl1KQKesw$QeKTzZY6uXZaqADuGkCAdVHhgDRdu5Z10v+7JWkKk5g=
# pbkdf2_sha256$870000$wB7Y3UjmlRyNNxLa6LH2BA$E50XJU1hlJ+S7+6aYbnvmen2/6YdxyjzJIr+lbTCT00=