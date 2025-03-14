from schProfile.serializers import schoolProfileSerializer
from schProfile.models import Profile
from .models import CustomUser
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
        }


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    profile = schoolProfileSerializer()
    user = authenticate(email=email, password=password)

    class Meta:
        model = CustomUser
        fields = ('email', 'username',  'password', 'profile')

    ''' def create(self, validated_data):
        profile_data = validated_data.pop('schProfile')
        user = CustomUser.objects._create_user(**validated_data)
        Profile.objects.create(**profile_data)
        return user
    '''
