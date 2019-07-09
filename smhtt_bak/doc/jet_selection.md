# Jet Selection

## inclusive jets

Kinematics:

```python
pt > 20 and
abs(eta) < 4.7
```

ID: [tight PF Jet ID](https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2017#Preliminary_Recommendations_for)

Overlap removal:

```python
dR(jet, l1) > 0.5 and
dR(jet, l2) > 0.5
```

## b-jets

To select b-jets, apply the following criteria to the selected inclusive jets.

Kinematics: tighten pseudorapidity range

```python
abs(jet.eta) < 2.5
```

b-tagging: [DeepCSV medium WP](https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X) with scale factors applied

```python
jet.bDiscriminator('pfDeepCSVDiscriminatorsJetTags:BvsAll') > 0.4941
```

Further details on how to apply b-tagging scale factors is provided [here](mc_corrections.md#b-tagging-scale-factors).


N.B.: CSVv2 discriminator is also available, but stated to be less performant compared to DeepCSV.
