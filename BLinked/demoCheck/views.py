from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from werkzeug.utils import secure_filename
from django.core.files.storage import default_storage
import json

import hashlib


from .merkletools import MerkleTools
from .blockchain import Blockchain




def verify(request):
    if request.method == 'POST':
        if 'json' not in request.FILES:
            # print error
            print("error")
        jsonFile = request.FILES['json']
        if jsonFile.name == '':
            print("file error")

        if jsonFile:
            jsonName = secure_filename(jsonFile.name)
            default_storage.save(jsonName, jsonFile)
            receiptJsonData = json.loads(default_storage.open(jsonName).read())

            print(jsonName)
            print(receiptJsonData)
            data = receiptJsonData['studentId'] + receiptJsonData['cpi'] + receiptJsonData['name'] + \
                   receiptJsonData['year'] + receiptJsonData['institution']
            print(data)

            data = data.encode()
            data = hashlib.sha3_256(data).hexdigest()

            mt = MerkleTools(hash_type='sha3_256')
            print("proof"+mt.validate_proof(receiptJsonData['merklePath'], data))
            merkleRoot = mt.validate_proof(receiptJsonData['merklePath'], data)
            res = False
            try:
                bc = Blockchain("VJTI")

                res = bc.verifyBatchMerkleRoot(receiptJsonData["institution"], receiptJsonData["year"], merkleRoot)
            except:
                print("Error occurred")

            if res is True:
                print("success")
            else:
                print("not success")


    template = loader.get_template('demoCheck/verify.html')
    context = {
    }

    return HttpResponse(template.render(context, request))
