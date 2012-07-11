import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from misitio.utilities.contenttype import createConsejoComunal

from misitio.contenttypes.testing import MISITIO_CONTENTTYPES_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class TestSetup(unittest.TestCase):

    layer = MISITIO_CONTENTTYPES_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.types = getToolByName(self.portal, 'portal_types')
    
    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        pid = 'misitio.contenttypes'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')
    
    def test_content_is_created(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        existing = self.types.objectIds()
        self.assertTrue('consejo_comunal' in existing)
        self.assertTrue('miembro' in existing)

    def test_content_allowed(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        createConsejoComunal(self.portal, 'Consejo Comunal Las Piedritas')
        self.cc = getattr(self.portal, 'consejo_comunal_las_piedritas')
        self.assertEqual(self.cc.getConstrainTypesMode(),1)
        self.assertEqual(('file','image','link','miembro'), tuple(self.cc.getImmediatelyAddableTypes()))
        
 
