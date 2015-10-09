Strategies for the NDN Forwarding Daemon (NFD)
=========


This repository contains **EXPERIMENTAL** forwarding strategies for [NFD](https://github.com/named-data/NFD). We currently provide the following strategies:

* Weighted Load Balancer: Uses the last RTT to bias next hop selection in favor of lower latency
* Random Load Balancer: Randomly (and statelessly) selects the next hop

The `tools` directory contains helper consumer and producer Python
scripts to test the strategies.

Requirements
------------

* A recent version of [NFD](https://github.com/named-data/NFD) (tested with 0.3.4). *Note: you will need to install NFD from source.*
* The corresponding version of [ndn-cxx](https://github.com/named-data/ndn-cxx) (e.g. 0.3.4)
* [PyNDN2](https://github.com/named-data/pyndn2) if you wish to use the helper tools.


Installation
----------

Installation is only necessary for the forwarding strategies. First,
copy contents of the directory of the strategies you wish to use into
`/<path-to-NFD/NFD/daemon/fw/`. Recompile NFD as normal.

To activate the strategies at runtime, use the `nfdc` tool (shipped
with NFD). The command `nfdc set-strategy /foo/bar /strategy/name`
where `/strategy/name` is the NDN name of the strategy you want to
enable for the namespace `/foo/bar`. For example:

```
# Enable the weighted load balancer strategy on namespace /hello/world

nfdc set-strategy /hello/world /localhost/nfd/strategy/weighted-load-balancer
```

Names for Available NDN strategies:

* **Weighted Load Balancer:** /localhost/nfd/strategy/weighted-load-balancer
* **Random Load Balancer:** /localhost/nfd/strategy/random-load-balancer







