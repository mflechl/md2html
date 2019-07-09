# JetMET uncertainties

## Jet energy scale (JES) uncertainties

The latest uncertainty files can be found here: 

* [Summer16](https://github.com/cms-jet/JECDatabase/blob/master/textFiles/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_UncertaintySources_AK4PFchs.txt)
* [Fall17](https://github.com/cms-jet/JECDatabase/blob/master/textFiles/Fall17_17Nov2017F_V6_DATA/Fall17_17Nov2017F_V6_DATA_UncertaintySources_AK4PFchs.txt)

These uncertainties can be applied by following [these recommendations](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#JetCorUncertainties).

The 2016 (2017) JES uncertainties consist of 27 (28) sources, these are uncertainties are provided both separately and added in quadrature to give the "Total" JES uncertainty. More information on the JES uncertainty sources can be found [here](https://twiki.cern.ch/twiki/bin/view/CMS/JECUncertaintySources).

It has been found in past SM analyses that using the Total JES uncertainty as 1 nuisance parameter leads to a very tight constrain on the JES uncertainty O(10%). This effect is due to central jets overly-constraining forwards jets. To remove this constraint JES sources are grouped regionally depending on whether the sources affect central detector regions (0<eta<3), the HF (eta>3) or the full detector (0<eta<5). The exceptions to this grouping are the "RelativeBal" and "RelativeSample" sources ("RelativeSample" is only included in the 2017 JES sources), these uncertainties in principle should affect the full detector region however, as these are unexpectedly large in the forwards regions, including them in the full region leads to a rather large constraint on the uncertainty so for this reason they are included as separate uncertainties. 

The naming convention for the regionally split uncertainties as well as the sources that should be combined are listed in the table below 

| Uncertainty name | Regions Affected | Sources | 
|--------|------------------------|---------|---------|
| {Process}_CMS_scale_j_eta0to5_13Tev{Up/Down} | 0 < eta < 5 | "SinglePionECAL", "SinglePionHCAL", "AbsoluteFlavMap", "AbsoluteMPFBias", "AbsoluteScale", "AbsoluteStat", "Fragmentation", "FlavorQCD", "TimePtEta", "PileUpDataMC", "RelativeFSR", "RelativeStatFSR", "PileUpPtRef" |
| {Process}_CMS_scale_j_eta0to3_13TeV{Up/Down} | 0 < eta < 3  | "PileUpPtEC1", "PileUpPtEC2", "PileUpPtBB", "RelativeJEREC1", "RelativeJEREC2", "RelativePtEC1", "RelativePtEC2", "RelativeStatEC", "RelativePtBB" |
| {Process}_CMS_scale_j_eta3to5_13TeV{Up/Down} | eta > 3       | "RelativeStatHF", "RelativePtHF", "PileUpPtHF", "RelativeJERHF" |
| {Process}_CMS_scale_j_RelativeBal_13TeV{Up/Down} | 0 < eta < 5 | "RelativeBal" | 
| {Process}_CMS_scale_j_RelativeSample_13TeV{Up/Down} (2017 only) | 0 < eta < 5 | "RelativeSample" |

**Note these groupings have only been checked so far for 2016. This should also be checked also for 2017.**

To group the uncertainties the up/down shift for each source should be calculated and added in quadrature to obtain the total shift. The total shift is then applied to all the jets in the event in the usual way. An example of how to do this can be found [here](https://github.com/danielwinterbottom/ICHiggsTauTau/blob/master/Analysis/HiggsTauTau/interface/JetEnergyUncertainty.h#L95-L120).

For all MC samples WITHOUT recoil corrections applied the JES uncertainty shifts should also be propagated to the MET (and any variables that depend on the MET e.g SV-fit mass). The shift to be applied to the MET is defined by summing together the 4-vectors of all jets in the collection before and after the JES shifts are applied. The MET shift is then the difference between the 2 resulting 4-vectors, after-before (see example [here](https://github.com/danielwinterbottom/ICHiggsTauTau/blob/master/Analysis/HiggsTauTau/interface/JetEnergyUncertainty.h#L95-L120)). This shift is then applied to the MET as in [this example](https://github.com/danielwinterbottom/ICHiggsTauTau/blob/7b8c2716da1949018614aadcde0fdeb635d61c27/Analysis/HiggsTauTau/src/HTTPairSelector.cc#L556-L562). The JES shifts should be applied to all jets passing the PFJet ID (i.e before the jet collection is filtered to remove any jets matched in dR to selected electron/muon/tau pair). 

## MET uncertainties 

For MC samples **WITHOUT recoil corrections** applied, the uncertainties due to the JES and un-clustered energy corrections should be used. For the JES uncertainty see the instructions above. For the un-clustered energy uncertainty instruction on how to compute this shift can be found [here](https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETUncertaintyPrescription). The MET uncertainty due to unclustered energy corrections should be named like:

```
{Process}_CMS_scale_met_unclustered_13TeV{Up/Down}
```

For MC samples **WITH recoil corrections** applied, the JES and un-clustered energy uncertainties are not applied. Instead, the systematic shifts related to the recoil "response" and "resolution" uncertainties should be applied. For information on how to apply these see [here](https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2017#Applying_MET_related_systematic). The recoil corrections are derived in 3 njets bins:

* njets=0
* njets=1,
* njets>1 

meaning the uncertainties for each njet bin should be propagated as separate nuisance parameters giving a total of 6 nuisance parameters (3 njets bins x {recoil\_response, recoil\_resolution} )

Remember when counting njetss for the W+jets MC, njets should be increased by 1 to account for the additional jet that fakes the hadronic-tau (or electron in the case of the em channel). Therefore, no njets=0 uncertainty need be applied for the W+jets MC. The MET uncertainties due to resolution should be named like:

```
{Process}_CMS_htt_boson_reso_met_0Jet_13TeV{Up/Down}
{Process}_CMS_htt_boson_reso_met_1Jet_13TeV{Up/Down}
{Process}_CMS_htt_boson_reso_met_2Jet_13TeV{Up/Down} 
```

And the MET uncertainties due to the response should be named like

```
{Process}_ CMS_htt_boson_scale_met_0Jet_13TeV{Up/Down}
{Process}_ CMS_htt_boson_scale_met_1Jet_13TeV{Up/Down}
{Process}_ CMS_htt_boson_scale_met_2Jet_13TeV{Up/Down} 
```