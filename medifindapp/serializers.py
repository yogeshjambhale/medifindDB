from rest_framework import serializers

from .models import User, Products,CartData,UserSignup,AdminSignup,Address,Orders,rooms,hotel




class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class CartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartData
        fields = "__all__"

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = "__all__"

class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSignup
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},read_only=True)
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs={
            'password':{'read_only':True}
        }

# validating password  
def validate(self,attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')   
    if password != password2:
        raise serializer.ValidationError("password & confirm password doesn't match")
    return sttrs

def create(self, validate_data):
    return User.objects.create(**validate_data)

class RoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = rooms
        fields = [
            'id',
            'hotel',
            'bedtypes',
            'roomtypes',
            'aminities',
            'totalbeds',
            'price',
            'images'
        ]
        # read_only_fields = ('hotel',)

class HotelSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True, read_only = True)
    
    class Meta:
        model = hotel
        fields = [
            'id',
            'hotel_name',
            'staytypes',
            'aminities',
            'description',
            'address',
            'images',
            'room'
        ]

    # def create(self, validated_data):
    #     room = validated_data.pop('room')
    #     hotels = hotel.objects.create(**validated_data)
    #     for Rooms in room:
    #         rooms.objects.create(**Rooms, hotels=hotels)
    #     return hotels

# {
#     "hotel_name":"jhvch",
#     "staytypes":"akjhjkbjs",
#     "aminities":"kdhajanms",
#     "description":"bachhbakba",
#     "address":"hjakj",
#     "images":"klknlas",
#     "room":{
#         "bedtypes":"jhvch",
#         "roomtypes":"akjnchjkbjs",
#         "aminities":"kdhassjanms",
#         "totalbeds":"bacashhbakba",
#         "price":"hjdakj",
#         "images":"klkaasxnlas"
#     }
# }