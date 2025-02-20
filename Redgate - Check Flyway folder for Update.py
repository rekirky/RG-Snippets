import urllib.request
import xmltodict
import re

prod_list = []

def version_compare(v1, v2):
    #Strip beta strings
    v1 = re.sub(r'-.*','',v1)
    v2 = re.sub(r'-.*','',v2)
    
    # Split version strings into integers    
    v1_parts = list(map(int, v1.split('.')))
    v2_parts = list(map(int, v2.split('.')))

    # Compare the major, minor, and patch version numbers in order
    for i in range(len(v1_parts)):
        # Newer version is higher, keep
        if v1_parts[i] < v2_parts[i]:
            return v2
        # Current version is higher, keep
        elif v1_parts[i] > v2_parts[i]:
            return v1
    # Versions are equal, keep current
    return v1

def get_flywaycli(prod_list):
    version = '0.0.0'
    product = []
    url = f"https://redgate-download.s3.eu-west-1.amazonaws.com/?delimiter=/&prefix=maven/release/com/redgate/flyway/flyway-commandline/"
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    for i in data["ListBucketResult"]["CommonPrefixes"]:
        product.append(i["Prefix"].replace("maven/release/com/redgate/flyway/flyway-commandline/","").replace("/",""))

    for i in range(len(product)):
        version = version_compare(version,product[i])
    url = f"{url}{version}/"
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    for x in data["ListBucketResult"]["Contents"]:
        if x["Key"].endswith("zip"):
            date = x["LastModified"]
    link = f"https://download.red-gate.com/maven/release/com/redgate/flyway/flyway-commandline/{version}"
    prod_list.append([{"product":f"Flyway CLI - {version}","link":link,"date":date}])
    print(version)
    return(prod_list)

get_flywaycli(prod_list)
