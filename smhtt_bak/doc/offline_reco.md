# Offline reconstruction

**This section is mostly copied from 2016 so far. Remove this comment once it has been checked.**


## Vertices

MiniAOD collection:
```
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<reco::Vertex>                 "offlineSlimmedPrimaryVertices"          ""                "PAT"
```

The primary vertex is the first one in the vertex collection.


## Electrons

MiniAOD collection:

```
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<pat::Electron>                 "slimmedElectrons"          ""                "YOUR_PROCESS"
```

According to the latest recommendations, the electrons collection must be recomputed in order to have V2 ID's
and scale & smear corrections. Therefore, access the collection from `YOUR_PROCESS`.

### Identification:

[EGammaPOG](https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPOG) recommendations & recipes:

* [Recommendations for 2017 data](https://twiki.cern.ch/twiki/bin/viewauth/CMS/Egamma2017DataRecommendations)
* [Details on MiniAODv2 contents](https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2)
* [MVA ID for Run 2](https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2)
* [Cut-based ID](https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2)

Following ID's are under consideration:

```
egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90
egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp80
egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wpLoose

egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto
egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-loose
egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-medium
egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-tight
```

The `noIso` version of the MVA-based ID's is chosen in ordner to optimize the isolation cut of the electrons
and to be able to defined isolation-inverted control regions.
For the selection of the signal pair, the `egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90`
is chosen according to studies presented by
[Albert Dow](https://indico.cern.ch/event/740095/contributions/3078671/attachments/1688876/2716798/HTT_18July18_Adow.pdf).
The study is performed on `V1` ID's in $`e\tau_{h}`$ channel and needs therefore a check on `V2` and in $`e\mu`$ channel.
Please also refer to [third lepton veto](baseline_selection.md#third-lepton-veto) and
[dilepton veto in $`e\tau_{h}`$ channel](baseline_selection_etau.md#di-electron-veto) for respective ID choices.


### Isolation

The isolation definition [recommended](https://hypernews.cern.ch/HyperNews/CMS/get/egamma/2094/2.html)
and supported by [EGammaPOG](https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPOG) is
the isolation corrected with the [effective area method](https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaPFBasedIsolationRun2#Rho_effective_area_corrections).
Here is the [NanoAOD implementation](https://github.com/cms-sw/cmssw/blob/8dd78b7350917467b53658824234f8a3e1bd815d/PhysicsTools/NanoAOD/plugins/IsoValueMapProducer.cc#L209).

dR = 0.3, total (with rho*EA PU corrections)

```
iso = (electron.pfIsolationR03().sumChargedHadronPt + max(0,
       electron.pfIsolationR03().sumNeutralHadronPt +
       electron.pfIsolationR03().sumPhotonPt -
       rho * effective_area)) / electron.pt()
```

where:

* rho = `fixedGridRhoFastjetAll`
* effective_area is defined below (please cross-check [here](https://github.com/cms-sw/cmssw/blob/master/RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt))

```
# This file contains Effective Area constants for
# computing pile-up corrections for the neutral hadron and photon
# isolation for an electron object.
#   Documentation:from
#
#   https://indico.cern.ch/event/697576/contributions/2940576/attachments/1620927/2578913/eleIdTuning.pdf
#   (slides 3 to 5)
#
#  The effective areas are based on 90% efficient contours
#
# For eta, use the eta of the supercluster
#
# |eta| min   |eta| max   effective area
0.000        	1.000			0.1440
1.000       	1.479       	0.1562
1.479        	2.000       	0.1032
2.000        	2.200       	0.0859
2.200        	2.300       	0.1116
2.300        	2.400       	0.1321
2.400 		   	2.500			0.1654
```

To be studied:

* the choice of cone sizes (signal and veto),
* the inclusion of $`e`$ or $`\mu`$ candidates in the charged isolation sum
* the pileup suppression ($`\Delta\beta`$, $`\rho`$-subtracted, PF-weighting, PUPPI, etc).


## Muons

MiniAOD collection:

```
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<pat::Muon>                     "slimmedMuons"              ""                "PAT"
```

### Identification

[MuonPOG](https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonPOG) recommendations & recipes:

* [Medium muon ID](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Medium_Muon). More info in [these slides](https://indico.cern.ch/event/357213/contribution/2/material/slides/0.pdf).

For the selection of the signal pair, **medium cut-based ID** is currently the sync default.
The SW recipe is well described in the link above.
Please also refer to [third lepton veto](baseline_selection.md#third-lepton-veto) and
[dilepton veto in $`\mu\tau_{h}`$ channel](baseline_selection_mutau.md#di-muon-veto) for respective ID choices.

### Isolation

For isolation, the default PF sums are taken as the baseline for a $`\Delta\beta`$-corrected isolation.

dR=0.4

```
iso = (muon.pfIsolationR04().sumChargedHadronPt + max(0.,
       muon.pfIsolationR04().sumNeutralHadronPt +
       muon.pfIsolationR04().sumPhotonPt -
       0.5 * muon.pfIsolationR04().sumPUPt)) / muon.pt()
```

To be studied:

* the choice of cone sizes (signal and veto),
* the inclusion of $`e`$ or $`\mu`$ candidates in the charged isolation sum
* the pileup suppression ($`\Delta\beta`$, $`\rho`$-subtracted, PF-weighting, PUPPI, etc).


## Taus

MiniAOD collection:

```
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<pat::Tau>                      "slimmedTaus"               ""                "YOUR_PROCESS"
```

According to the latest recommendations, the best performing ID's against jets (`byIsolation`) need to be computed on top of MiniAOD. Therefore, access the collection from `YOUR_PROCESS`.

### Identification

[TauPOG](https://twiki.cern.ch/twiki/bin/view/CMS/Tau) recommendations & recipes:

* [Tau ID recommendation 13 TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)
* [Details on running ID's on top of MiniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Rerunning_of_the_tau_ID_on_M_AN1)

Following discriminators are under consideration:

* Discrimination against jets (MVA-based):

```
byIsolationMVArun2017v2DBoldDMwLTraw2017
byVVLooseIsolationMVArun2017v2DBoldDMwLT2017
byVLooseIsolationMVArun2017v2DBoldDMwLT2017
byLooseIsolationMVArun2017v2DBoldDMwLT2017
byMediumIsolationMVArun2017v2DBoldDMwLT2017
byTightIsolationMVArun2017v2DBoldDMwLT2017
byVTightIsolationMVArun2017v2DBoldDMwLT2017
byVVTightIsolationMVArun2017v2DBoldDMwLT2017
```

* Discrimination against electrons (MVA-based):

```
againstElectronVLooseMVA6
againstElectronLooseMVA6
againstElectronMediumMVA6
againstElectronTightMVA6
againstElectronVTightMVA6
```

* Discrimination against muons (cut-based):

```
againstMuonLoose3
againstMuonTight3
```

* Please note, that studies and validation is ongoing for [DNN-based](https://indico.cern.ch/event/764184/contributions/3178902/attachments/1734126/2804004/mbluj_deepTauId_validation_followup_15Oct2018.pdf) Tau ID's
as well as a [new training](https://indico.cern.ch/event/763206/contributions/3168444/attachments/1729998/2795591/mbluj_newAntiE_validation_3Oct2018.pdf) for the anti-electron discriminator was performed and is under validation


## Jets

MiniAOD collection:

```
<verbatim>
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<pat::Jet>                      "slimmedJets"               ""                "YOUR_PROCESS"
```

In order to apply the latest jet energy corrections (JEC) available in a global tag (GT), the jets in MiniAOD need to be updated. Therefore, access the collection from `YOUR_PROCESS`.

### Identification

**Tight jet ID** is applied. Additionally, jets overlapping with electrons, muons or taus are removed.
Further details on selection are described [here](jet_selection.md#inclusive-jets).

[JetMETPOG](https://twiki.cern.ch/twiki/bin/view/CMS/JetMET) recommendations & recipes:

* [Jets in the MiniAOD](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017#Jets)
* [How to apply Jet Energy Corrections](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#CorrPatJets)
* [PF Jet ID (general)](https://twiki.cern.ch/twiki/bin/view/CMS/JetID)
* [Jet ID recommendations for 2017 data](https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID13TeVRun2017)
* [Pileup Jet ID](https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID)


## B-tagging

[BtagPOG](https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagPOG) recommendations & recipes:

* [General recommendations](https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation)
* [Discriminator working points for 2017 data](https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X)
* [Jet-by-jet application of b-tagging scale-factors](https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#2a_Jet_by_jet_updating_of_the_b)
* [Measurement of b-tagging efficiencies in MC](https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#b_tagging_efficiency_in_MC_sampl)

In MiniAODv2 the established b-tagging discriminators (CSVv2 and DeepCSV) are already stored within the jets.
The details on the b-jet selection are described [here](jet_selection.md#b-jets).
The **DeepCSV** discriminator is stated to perform better than the CSVv2, therefore, **DeepCSV** is chosen to select b-jets.
Still need a proper check of data/MC agreement for all b-taggers.
Please note, that it is also possible to use the **DeepFlavour** tagger on 2017 data.

## MET

MiniAOD collections:

```
Type                                  Module                      Label             Process
-------------------------------------------------------------------------------------------------
vector<pat::MET>                      "slimmedMETs"               ""                "YOUR_PROCESS"
vector<pat::MET>                      "slimmedMETsPuppi"          ""                "PAT"
```

These two collections correspond to the PFMET and to the PUPPI MET, respectively. Currently, PFMET is chosen as baseline.
Following the recent recommendations, PFMET needs to be corrected for EE noise and Type-1 re-corrected with MET recipe v2.
PUPPI MET should be Type-1 recorrected. Currently, it is not possible to (re-)correct both definitions of MET.
Therefore only the baseline PFMET is corrected, which can be accessed in `YOUR_PROCESS`.
PUPPI MET is used with corrections provided in MiniAOD computed within the `PAT` step.

Please note, that MVA MET based on DNN is under development and is planned to be ready for the Run 2 legacy papers. It will be applied on (sync) ntuple level. Particular instructions for needed inputs will be provided as soon as the software is ready to be used.

[JetMETPOG](https://twiki.cern.ch/twiki/bin/view/CMS/JetMET) recommendations & recipes:
* [Re-correction of MET (general)](https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#We_have_a_tool_to_help_you_to_ap)
* [EE noise mitigation for PFMET in 2017 data](https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_for_2)
* [MET Filters for 2017 data](https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2018)
