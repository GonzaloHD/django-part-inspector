from rest_framework import serializers
from .models import Part, Inspection, Feature



class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer): 
    # Remove part from being required in the serializer, so it's handled manually
    part = serializers.PrimaryKeyRelatedField(queryset=Part.objects.all(), required=False)     
    class Meta:
        model = Feature
        fields = '__all__'
        
class PartSerializer(serializers.ModelSerializer):
    # Using nested serializer to accept a list of features
    features = FeatureSerializer(many=True)

    class Meta:
        model = Part
        fields = '__all__'

    def create(self, validated_data):
        # Extract the features data from validated_data
        features_data = validated_data.pop('features')
        
        # Create the Part object first
        part = Part.objects.create(**validated_data)

        # Now, create each Feature and associate it with the Part
        for feature_data in features_data:
            # You can add custom logic here if needed, like checks or transformations
            feature_data['part'] = part
            Feature.objects.create(**feature_data)

        return part

    def update(self, instance, validated_data):
        # Update the Part object first
        features_data = validated_data.pop('features', [])
        
        # Update the Part itself
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Now, update or create Features
        for feature_data in features_data:
            # Handle creation or update for each feature
            feature_id = feature_data.get('id')
            if feature_id:
                # Update the existing feature
                feature = Feature.objects.get(id=feature_id)
                for attr, value in feature_data.items():
                    setattr(feature, attr, value)
                feature.save()
            else:
                # Create a new feature if no ID is provided
                feature_data['part'] = instance
                Feature.objects.create(**feature_data)

        return instance
