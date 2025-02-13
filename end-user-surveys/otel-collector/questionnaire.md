# OpenTelemetry Collector User Survey Questions

## Metadata
- issue: `TBD`
- questionnaire-link: `TBD`
- start: 2024-01-03
- end: 2024-01-31
- sample-size: 186

## Questions

#### 1. How many Collectors do you run in your organization?
- 1
- Between 2 and 5
- Between 5 and 10
- More than 10

#### 2. Where do you deploy your Collectors?
[[Multiple Choice]]
- Kubernetes
- Virtual Machine (VM)
- Bare Metal
- Other

#### 3. What deployment scenarios do you use your Collectors in?
- next to my application (i.e. k8s sidecar)
- On every host (i.e k8s daemonset)
- As a gateway (i.e. k8s deployment)
- In a stateful scenario (ie k8s statefulset)
- I don't deploy any Collectors to Kubernetes

#### 4. How do you deploy the OTel Collector on Kubernetes?
- OTel Collector Helm Chart
- OTel Operator
- My own manifests
- I don't deploy the OTel Collector on Kubernetes
- Other

#### 5. Do you build your own Collector distribution?
- Yes
- No

#### 6. Do you use the OTel Collector Builder to build your own OTel Collector distribution?
- Yes
- No

#### 7. How easy do you find it to build your own OTel Collector distributions with the Collector Builder?
- It's easy to use. I love it!
- Meh
- It's too hard to use!
- I don't use it

#### 8. How do you monitor your Collector?
[[Multiple Choice]]
- Logs
- Collector metrics
- I don't
- Other

#### 9. Which of the following Exporters do you use?
[[Multiple Choice]]
- alertmanagerexporter
- awscloudwatchlogsexporter
- awsemfexporter
- awskinesisexporter
- awss3exporter
- awsxrayexporter
- azuredataexplorerexporter
- azuremonitorexporter
- carbonexporter
- clickhouseexporter
- coralogixexporter
- datadogexporter
- debugexporter
- dynatraceexporter
- elasticsearchexporter
- fileexporter
- googlecloudexporter
- googlecloudpubsubexporter
- googlemanagedprometheusexporter
- honeycombmarkerexporter
- influxdbexporter
- instanaexporter
- kafkaexporter
- loadbalancingexporter
- loggingexporter
- logzioexporter
- lokiexporter
- opensearchexporter
- otlpexporter
- otlphttpexporter
- prometheusexporter
- prometheusremotewriteexporter
- pulsarexporter
- sapmexporter
- sentryexporter
- signalfxexporter
- skywalkingexporter
- splunkhecexporter
- sumologicexporter
- syslogexporter
- zipkinexporter
- None

#### 10. Which of the following receivers do you use?
[[Multiple Choice]]
- activedirectorydsreceiver
- aerospikereceiver
- apachereceiver
- apachesparkreceiver
- awscloudwatchmetricsreceiver
- awscloudwatchreceiver
- awscontainerinsightreceiver
- awsecscontainermetricsreceiver
- awsfirehosereceiver
- awsxrayreceiver
- azureblobreceiver
- azureeventhubreceiver
- azuremonitorreceiver
- bigipreceiver
- carbonreceiver
- chronyreceiver
- cloudflarereceiver
- collectdreceiver
- couchdbreceiver
- datadogreceiver
- dockerstatsreceiver
- elasticsearchreceiver
- expvarreceiver
- filelogreceiver
- filereceiver
- filestatsreceiver
- flinkmetricsreceiver
- fluentforwardreceiver
- gitproviderreceiver
- googlecloudpubsubreceiver
- googlecloudspannerreceiver
- haproxyreceiver
- hostmetricsreceiver
- httpcheckreceiver
- iisreceiver
- influxdbreceiver
- jaegerreceiver
- jmxreceiver
- journaldreceiver
- k8sclusterreceiver
- k8seventsreceiver
- k8sobjectsreceiver
- kafkametricsreceiver
- kafkareceiver
- kubeletstatsreceiver
- lokireceiver
- memcachedreceiver
- mongodbatlasreceiver
- mongodbreceiver
- mysqlreceiver
- namedpipereceiver
- nginxreceiver
- nsxtreceiver
- opencensusreceiver
- oracledbreceiver
- osqueryreceiver
- otlpjsonfilereceiver
- otlpreceiver
- postgresqlreceiver
- prometheusreceiver
- pulsarreceiver
- rabbitmqreceiver
- receivercreator
- redisreceiver
- riakreceiver
- sapmreceiver
- signalfxreceiver
- simpleprometheusreceiver
- snmpreceiver
- solacereceiver
- splunkhecreceiver
- sqlqueryreceiver
- sqlserverreceiver
- sshcheckreceiver
- statsdreceiver
- syslogreceiver
- tcplogreceiver
- udplogreceiver
- vcenterreceiver
- webhookeventreceiver
- windowseventlogreceiver
- windowsperfcountersreceiver
- zipkinreceiver
- zookeeperreceiver
- None

#### 11. Which of the following processors do you use?
[[Multiple Choice]]
- attributesprocessor
- batchprocessor
- cumulativetodeltaprocessor
- datadogprocessor
- deltatorateprocessor
- filterprocessor
- groupbyattrsprocessor
- groupbytraceprocessor
- k8sattributesprocessor
- logstransformprocessor
- memorylimiterprocessor
- metricsgenerationprocessor
- metricstransformprocessor
- probabilisticsamplerprocessor
- redactionprocessor
- remotetapprocessor
- resourcedetectionprocessor
- resourceprocessor
- routingprocessor
- schemaprocessor
- servicegraphprocessor
- spanmetricsprocessor
- spanprocessor
- tailsamplingprocessor
- transformprocessor
- None

#### 12. Which of the following connectors do you use?
[[Multiple Choice]]
- countconnector
- datadogconnector
- exceptionsconnector
- failoverconnector
- forwardconnector
- routingconnector
- servicegraphconnector
- spanmetricsconnector
- None

#### 13. Which of the following extensions do you use?
[[Multiple Choice]]
- asapauthextension
- awsproxy
- basicauthextension
- bearertokenauthextension
- encoding
- filestorage
- headerssetterextension
- healthcheckextension
- httpforwarder
- jaegerremotesampling
- memory_ballast
- oauth2clientauthextension
- observer
- oidcauthextension
- opampextension
- pprofextension
- remotetapextension
- sigv4authextension
- storage
- zpages
- None

#### 14. What kind of improvement would you most like to see for the Collector?
- Stability
- Configuration management and resolution
- Collector observability
- Support for more receivers or exporters
- Other
[[Single Line Text Box]]
