# OpenTelemetry and Prometheus Interoperability Survey Questions

## Metadata
- issue: `TBD`
- questionnaire-link: `TBD`
- start: 2024-05-01
- end: 2024-05-31
- sample-size: 91

## Questions

#### 1. How large is your organization?
- 0-50
- 50-100
- 100-1,000
- \>1,000

#### 2. What industry do you work in?
- Technology
- Manufacturing
- Aerospace
- Retail
- Finance
- Healthcare
- Automotive
- Hospitality
- Research
- Travel & Leisure
- Media
- Advertisement
- Other

#### 3. What type of team do to work on?
- Dev
- DevOps
- Operations
- SRE
- Platform Engineering
- Observability
- System Administration
- Sales Engineering
- DevRel
- Other

#### 4. How well do you understand Prometheus?
[[Components]]
- LIBRARIES
- FORMATS
- SERVER CONFIGURATION
- PROMQL

[[Rating choices]]
- Not at all familiar
- Somewhat familiar
- Expert

#### 5. How familiar are you with OpenTelemetry?
[[Components]]
- LIBRARIES
- OTLP
- COLLECTOR
- OPERATOR

[[Rating choices]]
- Not at all familiar
- Somewhat familiar
- Expert

#### 6. Which of the following instrumentation libraries or tools are you using (select all that apply):
[[Multiple Choice]]
- Prometheus Client Libraries
- Prometheus exporters (e.g. node_exporter)
- OpenTelemetry Metric Client Libraries
- OpenTelemetry Trace Client Libraries
- OpenTelemetry auto-instrumentation agents
- Other

#### 7. Which of the following OpenTelemetry components are you using to deliver metrics to your backend (select all that apply):
[[Multiple Choice]]
- OpenTelemetry Language SDK Prometheus exporters
- OpenTelemetry Language SDK Prometheus bridges
- OpenTelemetry Collector Prometheus receiver
- OpenTelemetry Collector Simple Prometheus receiver
- OpenTelemetry Collector Prometheus exporter
- OpenTelemetry Collector Prometheus remote write exporter
- Prometheus Client OTLP export
- Prometheus Server OTLP ingestion
- None of the Above
- Other

#### 8. Which of the following are you using to store metrics (select all that apply):
[[Multiple Choice]]
- The Prometheus Server
- An open-source prometheus backend (Thanos, Cortex, Grafana Mimir, etc.)
- A Prometheus-compatible (or PromQL compatible) solution from a vendor
- A backend not associated with Prometheus, not compatible with PromQL
- Other

#### 9. Which query language are you using to query metrics (select all that apply):
[[Multiple Choice]]
- PromQL
- SQL
- A vendor-specific query language (specify what under Other)
- A different open source query language (specify what under Other)
- Other

#### 10. Which of these have you done in the past 6 months (select all that apply):
[[Multiple Choice]]
- Added a metric to an application
- Configured collection or routing of metrics
- Written a live (ad-hoc) query over metrics
- Created or edited a dashboard for displaying metrics
- Created or edited an alert
- Created or edited a recording rule
- Other

#### 11. How easy have you found it to use OpenTelemetry with Prometheus?
- 1
- 2
- 3
- 4
- 5

#### 12. How confusing have you found the translation between OpenTelemetry metrics and Prometheus metrics?
- 1
- 2
- 3
- 4
- 5

#### 13. What have been the biggest challenges you've faced using OpenTelemetry with Prometheus?
[[Multi-Line Text Box]]

#### 14. What would you like to see changed or improved with OpenTelemetry's Prometheus support?
[[Multi-Line Text Box]]

#### 15. OpenTelemetry defines the HTTP server histogram metric as http.server.request.duration, with a unit of seconds (s). Suppose you are writing a query for the 95th percentile of the same HTTP metric. Which of the following would you expect to write (regardless of what is valid/correct today), (select all that apply):
[[Multiple Choice]]
- histogram_quantile(0.95, rate({"http.server.request.duration"}[5m]))
- histogram_quantile(0.95, rate({"http.server.request.duration_seconds"}[5m]))
- histogram_quantile(0.95, rate({"http.server.request.duration_seconds_bucket"}[5m]))
- histogram_quantile(0.95, rate({"http.server.request.duration_bucket"}[5m]))
- histogram_quantile(0.95, rate(http_server_request_duration_bucket[5m]))
- histogram_quantile(0.95, rate(http_server_request_duration_seconds_bucket[5m]))

#### 16. Suppose you've defined your own OpenTelemetry metric in Go to track how far your robot has traveled:

counter, _ := meter.Float64ObservableCounter("robot.distance.traveled",
       metric.WithUnit("mm")
   )
   // Call counter.Add() each time the robot moves.

Which of the following would you expect to write (regardless of what is valid/correct today), (select all that apply):
[[Multiple Choice]]
- rate({"robot.distance.traveled"}[5m])
- rate({"robot.distance.traveled_millimeters"}[5m])
- rate({"robot.distance.traveled_millimeters_total"}[5m])
- rate({"robot.distance.traveled_total"}[5m])
- rate(robot_distance_traveled[5m])
- rate(robot_distance_traveled_millimeters_total[5m])

#### 17. Imagine you know that your node's OpenTelemetry instrumentation defines a node.time metric, but you don't remember its unit. Someone complains about a flaky alert, so you open a YAML file with your alert configuration. Which of the following you prefer the most (select all that apply):
[[Multiple Choice]]
- expr: timestamp(node_time) - (1e-9 * node_time) >  5
- expr: timestamp({"node.time"}) - (1e-9 * {"node.time"}) >  5
- expr: timestamp(node_time_nanoseconds) - (1e-9 * node_time_nanoseconds) >  5
- expr: timestamp({"node.time_nanoseconds"}) - (1e-9 * {"node.time_nanoseconds"}) >  5

#### 18. Which of the following describes your opinion on units in metric names (select one):
- Units should be required to be part of the metric name. Without them, it is hard to write proper queries, write or read alerts e.g. in YAML, and build dashboards.
- Units should generally not be added to metric names. Instead, units should be separate metadata, like the metric description. If you need to know the units for queries in alerts and dashboards, you will go look them up.
- Units should generally not be added to metric names, but base units (seconds, meters, etc.) should be required.
- We should recommend adding units to metric names, for the reasons above, but let users decide if they should add them or not.
- I don't care, but just don't break whatever the current behavior is.

#### 19. Which of the following describes your opinion on dots vs underscores in metric names (select one):
- I like the dots better, and am glad OpenTelemetry chose to use them in metric names, let's make sure dots works better in Prometheus
- All dots should be changed to underscores when translating to Prometheus. That way, metric names match the format used by the rest of the Prometheus ecosystem.
- I wish OpenTelemetry had chosen to use underscores to match Prometheus syntactic requirements, I believe this decision should be revisited, it's worth the time and breaking existing OTel users.
- I don't care, but don't modify OpenTelemetry metric names.
- I don't care, but don't break whatever the current behavior is. 
