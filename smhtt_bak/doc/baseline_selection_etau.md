# Baseline Selection: e-tau


## electron

Kinematics:

```python
ele.pt() > 25 and
abs(elec.eta()) < 2.1
```

Vertex:

```c++
fabs(elec.gsfTrack()->dxy(vtx.position())) < 0.045 &&
fabs(elec.gsfTrack()->dz(vtx.position()))  < 0.2
```

ID: [recommendations for 2017 data](https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2#Recommended_MVA_Recipe_V2_for_re)

```python
MVA ID 90% efficiency WP 'egmGsfElectronIDs:mvaEleID-Fall17-noIso-V2-wp90'
```

In addition to the MVA ID, also require that the electron has no matched conversions and that the number of missing hits is <=1:

```c++
elec.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS))) <=1 &&
elec.passConversionVeto()
```

## tau

Kinematics:

```python
tau.pt() > 20 and fabs(tau.eta()) < 2.3
```

ID: [TauIDRecommendation13TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)

```python
tau.tauID('decayModeFinding') > 0.5                  and
'byVVLooseIsolationMVArun2017v2DBoldDMwLT2017'       and
tau.charge() in [1,-1]
```

Vertex:

```c++
pat::PackedCandidate const* packedLeadTauCand = dynamic_cast<pat::PackedCandidate const*>(src.leadChargedHadrCand().get())
fabs(packedLeadTauCand->dz()) < 0.2  # The PackedCandidate::dz() method is wrt. the first PV by default
```

## e-tau pair

```python
dR(e,tau) > 0.5
```

Require the single lepton trigger path listed in [the trigger section](trigger_info.md#e-tau-triggers), matching with HLT objects within $`\Delta R<0.5`$.

## Final selection (post sync ntuple)

### electron

Isolation:

```python
iso < 0.15
```

### tau

[TauIDRecommendation13TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)

* ID

```python
tau.tauID('againstElectronTightMVA6')      > 0.5  and
tau.tauID('againstMuonLoose3')              > 0.5
```

* Isolation: run2 MVA, oldDMs

```python
tau.tauID('byTightIsolationMVArun2017v2DBoldDMwLT2017') > 0.5
```

### Di-electron veto

Set this flag if there is an opposite-charge electron pair in the event with electrons separated by dR>0.15 and both passing the loose selection (the `dz`, `dxy` and `iso` variables are defined as for the nominal object selection above):

```python
elec.pt() > 15                                                                            and
fabs(elec.eta()) < 2.5                                                                    and
Fall17 cut-based 'Veto' ID 'egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto'      and
dz  < 0.2                                                                                 and
dxy < 0.045                                                                               and
iso < 0.3
```

**Important**: The cut-based electron ID is described [here](https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Offline_selection_criteria_for_V). This includes cuts on `d0, dz` and the rho-subtracted isolation. For consistency with our own analysis selection these cuts should be replaced with the `dxy, dz` and `iso` cuts listed above. A comparison with the full POG definition should be studied. **TODO: remove own isolation cut completely, since already optimized in the ID?**


### Third lepton veto

See definition [below](#third-lepton-veto), common to all channels. Reject event if any electron or muon (excluding signal electron) passes this selection.

