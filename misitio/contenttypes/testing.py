from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from zope.configuration import xmlconfig

class MisitioContenttypes(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import misitio.contenttypes
        xmlconfig.file('configure.zcml',
                       misitio.contenttypes,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'misitio.contenttypes:default')

MISITIO_CONTENTTYPES_FIXTURE = MisitioContenttypes()
MISITIO_CONTENTTYPES_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MISITIO_CONTENTTYPES_FIXTURE, ),
                       name="MisitioContenttypes:Integration")
