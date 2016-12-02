(function(nx, global) {
    nx.define('demo.TopologyViaApi', nx.ui.Component, {
        view: {
            props: {
                'class': "demo-topology-via-api"
            },
            content: {
                name: 'topology',
                type: 'nx.graphic.Topology',
                props: {
                    showIcon: true,
                    theme: 'green',
                    identityKey: 'id',
                    data: '{#topologyData}',
                    width: 700,
                    height: 700,
                    nodeConfig: {
                        iconType: "model.device_type",
                        label: "model.name"
                    }
                }
            }
        },
        properties: {
            topologyData: {}
        },
        methods: {
            init: function(options) {
                this.inherited(options);
                this.loadRemoteData();
            },
            loadRemoteData: function() {
                // CAUTION you must resolve the cross-domain problem in you own environment!
                var URL_TOPOLOGY = 'http://127.0.0.1:7778/data';
                $.ajax({
                    url: URL_TOPOLOGY,
                    success: function(data) {
                        this.topologyData(data);
                    }.bind(this)
                });
            }
        }
    });
})(nx, nx.global);
