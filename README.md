# tap-fbpageinsights

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Facecbook Page Insights](http://example.com)

---

Config File:

A tap_config file must be create as:

```
{
  "access_key": "Facecbook Page Token",
  "page_id": "Page Id",
  "start_date": "2019-02-21",
  "end_date": "2019-02-21"
}
```
Copyright &copy; 2018 Stitch
