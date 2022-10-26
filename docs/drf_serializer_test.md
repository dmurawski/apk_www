from class3app.models import Druzyna <br />
from class3app.serializers import DruzynaSerializer <br />
from rest_framework.renderers import JSONRenderer <br />
from rest_framework.parsers import JSONParser <br />
druzyna = Druzyna(nazwa='REAL MADRYT', kraj='ES') <br />
druzyna.save() <br />
serializer = DruzynaSerializer(druzyna) <br />
serializer.data <br />
content = JSONRenderer().render(serializer.data) <br />
content <br /><br />
import io <br />
stream = io.BytesIO(content) <br />
data = JSONParser().parse(stream) <br />
deserializer = DruzynaSerializer(data=data) <br />
deserializer.is_valid() <br />
deserializer.errors <br />
deserializer.fields <br />
repr(deserializer) <br />
deserializer.validated_data<br />
deserializer.save()<br />
deserializer.data<br />
<br />
<br />
from class3app.models import Osoba<br />
from class3app.serializers import OsobaSerializer<br />
from rest_framework.renderers import JSONRenderer<br />
from rest_framework.parsers import JSONParser<br />
osoba = Osoba(imie='Janusz', nazwisko='Tracz',data_dodania='2022-10-10')<br />
druzyna.save()<br />
serializer = OsobaSerializer(osoba)<br />
serializer.data<br />
content = JSONRenderer().render(serializer.data)<br />
content<br /><br />
import io<br />
stream = io.BytesIO(content)<br />
data = JSONParser().parse(stream)<br />
deserializer = OsobaSerializer(data=data)<br />
deserializer.is_valid()<br />
deserializer.errors<br />
deserializer.fields<br />
repr(deserializer)<br />
deserializer.validated_data<br />
deserializer.save()<br />
deserializer.data<br />