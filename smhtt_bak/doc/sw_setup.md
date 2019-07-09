# Software setup to run with latest update-recipes on MiniAOD

This section describes the setup, that can be used to run with latsest recipes on the MiniAOD files available.

## CMSSW Release and Global Tag

* release: `CMSSW_9_4_11_cand2` (used for SM HTT currently), latest available: `CMSSW_9_4_11_patch1`
* global tags:	
	* Data: `94X_dataRun2_v10`, contains the `V6` JEC for Data
	* MC: `94X_mc2017_realistic_v15`, contains the `V8` JEC for MC which is equivalent to `V6` in terms of corrections

In general, the latest available CMSSW release should be used for a new production.
To keep track of this, subscribe to the [Software Release Announcements HyperNews](https://hypernews.cern.ch/HyperNews/CMS/get/relAnnounce.html).
The reason to do this: in that way you profit from latest available bugfixes and backports in order to minimize the amount of merge-topics to be done.


To get the information on the latest Global Tags available, please consult first the [PdmV Analysis Summary Table](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable).
In that way you will find out, which syntax is followed by the Global Tags for a certain **data-taking** and **MC production**.
Some other websites to get similar information:
* [Frontier Conditions](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideFrontierConditions)
* [MiniAOD Workbook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD)
* PdmV Analysis pages:
    * [PdmV Analysis 2016](https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2016Analysis)
    * [PdmV Analysis 2017](https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2017Analysis)
    * [PdmV Analysis 2018](https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2018Analysis)

Please keep in mind, that the information on these pages could be outdated.
The first instance to search for newest Global Tags and conditions is [CMS Conditions DB Browser](https://cms-conddb.cern.ch/cmsDbBrowser/index/Prod).
If you know the syntax of a Global Tag you want to have, you can search for it omitting the version number, e.g. `94X_dataRun2_v` in case of 2016 and 2017 data.
Then, increase the number of shown results and order by **Snapshot Time**, latest time at the top.
The latest available version should be the one at the top with a **meaningful** Snapshot Time.
Don't forget to look at the difference between two Global Tags in the table to keep track of the changes happened between the two versions for the various records.
It is important that the Global Tags for data and MC have **consistent** JEC records. Therefore, `94X_mc2017_realistic_v15` should be used for MC and **not** `94X_mc2017_realistic_v16`

## Checkout script with latest recipes

Addional checkout needs to be done for the following updates:
* SM signal: working version of **HTXSRivetProducer** (relevant for SM $`H\rightarrow\tau\tau`$). Under `CMSSW_9_4_11_cand1`, a newer version is validated.
* Jets: latest DeepFlavour b-tagger discriminator (optional). For details, see at [DeepJet Twiki](https://twiki.cern.ch/twiki/bin/view/CMS/DeepJet#94X_installation_recipe_X_10)
* Electrons: need to rerun the scale & smear corrections to avoid a bug and compute V2 ID's
* PFMET: Type-1 recorrection with EE noise mitigation
* Taus: computation of multivariate ID's
    * against jets: BDT-based (MVAFall17v2), deep Tau (optional), DPF Tau (optional)
    * against electrons: new MVA training for 2017 campaigns (optional)

The bash script with various comments on the additional packages can be found under [scripts/checkout_94X.sh](../scripts/checkout_94X.sh).
Additionaly, a code snippet for `cmsRun` is provided under [scripts/cmsRunSnippet_cfg.py](../scripts/cmsRunSnippet_cfg.py) in order to summarize all additional sequences to be run.
Keep in mind, that this is not a fully functional `cmsRun` configuration file. Feel free to extend it accordingly.
