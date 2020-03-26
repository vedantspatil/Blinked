from django import forms

class EditDetailsForm(forms.Form):


    schoolName = forms.CharField(label='School Name', max_length=100)
    degree = forms.CharField(label='Degree', max_length=100)
    fieldOfStudy = forms.CharField(label='Field of study', max_length=100)
    startYear = forms.IntegerField(label='Start Year', required=False)
    endYear = forms.IntegerField(label='End Year', required=False)
    additionalNotes = forms.CharField(label='Additional Notes', max_length=1024, required=False)
    json = forms.FileField(label='Upload JSON Certificate')



    """

    <p>School Name *</p>
    <input type="text" name="school" required>
    <p>Degree *</p>
    <input type="text" name="degree" required>
    <p>Field of study *</p>
    <input type="text" name="fieldOfStudy" required>
    <p>Start Year</p>
    <input type="number" name="startYear">
    <p>End Year</p>
    <input type="number" name="endYear">
    <p>Additional Notes</p>
    <input type="text" name="additionalNotes">
    <p>Upload JSON Certificate</p>
    <input type="file" name="json" autocomplete="off" required>

    your_name = forms.CharField(label='Your name', max_length=100)
    """