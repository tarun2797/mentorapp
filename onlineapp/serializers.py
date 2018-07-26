from rest_framework import serializers
from onlineapp.models import college, Student, MockTest1


class collegeSerializer(serializers.Serializer):
    #id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    acronym = serializers.CharField(max_length=100)
    contact = serializers.EmailField()

    def create(self, validated_data):
        return college.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance

class MocktestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('problem1','problem2','problem3','problem4','total')

class StudentSerializer(serializers.ModelSerializer):
    mocktest1 = MocktestSerializer()
    class Meta:
        model = Student
        fields = ('id','name','dob','email','db_folder','dropped_out','college_id','mocktest1')

    def create(self,validated_data):
        #for i in validated_data.items():
        #    print("val = ",i)
        mock_data = validated_data.pop('mocktest1')

        student  = Student.objects.create(**validated_data)

        #stu_data = Student.objects.values().filter(name=student)
        MockTest1.objects.create(students=student,**mock_data)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.email = validated_data.get('email', instance.email)
        instance.db_folder = validated_data.get('db_folder', instance.db_folder)
        instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
        mock_data = validated_data.pop('mocktest1')
        #print("validted_data = ", validated_data)
        #print("mock_data = ",mock_data)
        instance.save()
        return instance

