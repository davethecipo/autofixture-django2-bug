from project.wsgi import application
from store.models import Another

from autofixture import AutoFixture
fixture = AutoFixture(Another, generate_m2m={'stuff': (1, 3)})
entries = fixture.create(1)