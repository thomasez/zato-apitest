
Given XPath "{xpath}" in request is a random string
=============================================================================================================

Usage example
-------------

```
Feature: zato-apitest docs

Scenario: Given XPath "{xpath}" in request is a random string

    Given address "http://apitest-demo.zato.io"
    Given URL path "/demo/xml"
    Given format "XML"
    Given request is "<req><howdy>foo</howdy></req>"
    Given XPath "//howdy" in request is a random string

    When the URL is invoked

    Then status is "200"
```

Discussion
----------

(None)