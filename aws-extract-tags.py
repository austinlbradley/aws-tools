import boto3

region = "us-east-1"
ec2 = boto3.resource("ec2",region_name=region)

def get_tag_key_value(tags, k):
    """Iterate instance tags for key and return the value as string."""
    for tag in tags:
        if tag["Key"].lower() == k.lower():
            return tag["Value"]
    return None

def extract_tags():
    """
    Shutdown, terminate expired instances, or start, stop scheduled instances and 
    return boto3 result as json, error as string, or None.
    """
    for instance in ec2.instances.all():

        if instance.tags:
            for t in instance.tags:
                if t["Key"] == "Name":
                    name = t["Value"]

        print("----------{}----------".format(name))

        attributes = ["id", "instance_type", "launch_time"]
        
        for a in attributes:
            print("{}: {}".format(a, getattr(instance, a)))
        
        print("state: {}".format(instance.state["Name"]))
        print("tags:")

        if instance.tags:
            for t in instance.tags:
                print("\t{}: {}".format(t["Key"],t["Value"]))

        print("\n")

if __name__ == "__main__":
    extract_tags()