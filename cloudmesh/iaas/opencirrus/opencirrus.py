from cloudmesh.iaas.ComputeBaseType import ComputeBaseType
from pprint import pprint
import cloudmesh
from sh import ssh


class openstack(ComputeBaseType):
    pass



    def connect(self):
        """connect to the cloud"""


        mesh = cloudmesh.mesh()
        cloudname = "sierra_openstack_grizzly"



        raise NotImplementedError()

    def config(self, dict):
        """uses the dict to conduct some configuration with the parameters passed"""
        raise NotImplementedError()

    def find_user_id(self, force=False):
        """finds the user id of a user and caches it. If a chaced
        value is ther it will use that. If you specify force, it will
        regenerate it"""
        self.user_id = "unkown"
        raise NotImplementedError()


    def _get_image_dict(self):
        raise NotImplementedError()

    def _get_flavors_dict(self):
        r = literal_eval(ssh ("username@servername", "cm list flavors"))
        return r

    def _get_servers_dict(self):
        raise NotImplementedError()

    def vm_create(self, name=None,
                  flavor_name=None,
                  image_id=None,
                  security_groups=None,
                  key_name=None,
                  meta=None):
        """create a virtual machine with the given parameters"""
        raise NotImplementedError()

    def vm_delete(self, id):
        """delete the virtual machine with the id"""
        raise NotImplementedError()

    def vms_project(self, refresh=False):
        raise NotImplementedError()

    def rename(self, old, new, id=None):
        """rename the firtual machine with the name old to the name new"""
        raise NotImplementedError()

    def usage(self, start, end, format='dict'):
        """returns the usage data between start and end date"""
        raise NotImplementedError()

    def limits(self):
        """returns a dict of limits that the cloud will maintain for a user and/or the project"""
        raise NotImplementedError()


    def keypair_list(self):
        raise NotImplementedError()

    def keypair_add(self, keyname, keycontent):
        raise NotImplementedError()

    def keypair_remove(self, keyname):
        raise NotImplementedError()
