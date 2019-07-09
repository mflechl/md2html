# Baseline tau-tau


## tau

Kinematics:

```python
tau.pt() > 40 and
abs(tau.eta()) < 2.1 and
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
fabs(packedLeadTauCand->dz()) < 0.2
```

## tau-tau pair

```python
dR(tau_1, tau_2) > 0.5
```

Require the trigger path listed in [the trigger section](trigger_info.md#tau-tau-triggers), matching the offline objects with the HLT objects with $`\Delta R<0.5`$.

After applying the pair selection detailed above order taus in the selected the di-tau pair by decreasing pT.

## Final selection (post sync ntuple)

### tau

[TauIDRecommendation13TeV](https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV)

* ID

```python
tau.tauID('againstElectronVLooseMVA6')      > 0.5  and
tau.tauID('againstMuonLoose3')              > 0.5  and
```

Isolation: run2 MVA, oldDMs

```python
tau.tauID('byTightIsolationMVArun2017v2DBoldDMwLT2017') > 0.5
```

### Third lepton veto

See [definition](baseline_selection.md#third-lepton-veto), common to all channels. Reject event if any electron or muon passes this selection.

