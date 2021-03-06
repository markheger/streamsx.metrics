
#Imports
from streamsx.topology.topology import *
from streamsx.topology.context import *
from streamsx.topology.schema import CommonSchema, StreamSchema
from streamsx.topology import context
from streamsx.spl.toolkit import add_toolkit
import streamsx.spl.op as op


monitoring_toolkit = '../com.ibm.streamsx.monitoring'
sample_toolkit = 'com.ibm.streamsx.monitoring.system.sample.LogSource'

def _launch(main):
    cfg = {}
    cfg[context.ConfigParams.SSL_VERIFY] = False
    rc = context.submit('DISTRIBUTED', main, cfg)

def monitor_app():
    topo = Topology('LogsMonitorSample')
    add_toolkit(topo, monitoring_toolkit)
    add_toolkit(topo, sample_toolkit)
    r = op.main_composite(kind='com.ibm.streamsx.monitoring.system.sample.LogSource::Monitor', toolkits=[monitoring_toolkit,sample_toolkit])
    _launch(r[0])

def sample_app():
    topo = Topology('LogsSample')
    add_toolkit(topo, monitoring_toolkit)
    add_toolkit(topo, sample_toolkit)
    r = op.main_composite(kind='com.ibm.streamsx.monitoring.system.sample.LogSource::SampleJob', toolkits=[monitoring_toolkit,sample_toolkit])
    _launch(r[0])


monitor_app()
sample_app()



