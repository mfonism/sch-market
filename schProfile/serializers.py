from rest_framework import serializers
from .models import schoolProfile
from register.models import CustomUser

class schoolProfileSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(source='pk', read_only=True)
  email = serializers.CharField(source='user.email', read_only=True)
  username = serializers.CharField(source='user.username', read_only=True)

  class Meta:
    model = schoolProfile
    fields = ( 'email', 'id', 'username', 'school_name',
              'address', 'badge', 'gender', 'level',
              'state', 'curriculum', 'extra_curriculum_activities',
              'website', 'clubs', 'school_phone_number', 'school_type',
              'school_email', 'school_facilities', 'awards_won', 'date_established',
              'school_fees_range', 'motto'
    )

  def create(self, validated_data, instance=None):
    if 'user' in validated_data:
      user = validated_data.pop('user')
    else:
      user = CustomUser.objects.create(**validated_data)
    profile, created_profile = schoolProfile.objects.update_or_create(user=user, **validated_data)
    return profile
