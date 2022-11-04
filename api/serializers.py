from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyric
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()

class UserInputSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ('email','first_name','last_name','password', 'password2')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return super().validate(attrs)

class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','email','first_name','last_name')

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id','first_name','last_name','age')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id','title','artiste_id', 'date_released', 'likes')

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ('id','song_id','content')