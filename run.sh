# To NOT submit, change 'python submitProdStep.py ...' to 'python submitProdStep.py -S ...'

# GS, DIGI, RECO steps
for eta in 21; do for pT in 50; do python submitProdStep.py -w 23293.0_CloseByParticleGun+2026D49+CloseByParticle_Photon_ERZRanges_GenSimHLBeamSpotHGCALCloseBy+DigiTrigger+RecoGlobal+HARVESTGlobal --nRuns=100 -n 1000 --pT=${pT} --pdgid=22 --minZ=320 --maxZ=320.001 --minEta=${eta}-0.0001 --maxEta=${eta}+0.0001 -d Photons/FineCalo --config1=../CloseByParticle_Photon_ERZRanges_cfi_GEN_SIM.py -o ProdTicl/ -e /eos/cms/store/group/dpg_hgcal/comm_hgcal/bainbrid --PtEta=pt${pT}_eta${eta}; done; done

# TICL RERECO
#for eta in 21; do for pT in 50; do python submitProdStep.py --nRuns=100 -n 0 -d Photons --skip-step1 --skip-step2 --skip-step3 --configTicl=step3ticl_noPU.py -o ProdTicl/ -e /eos/cms/store/group/dpg_hgcal/comm_hgcal/bainbrid/Photons/samples/FineCalo/220406/step3ticl -E /eos/cms/store/group/dpg_hgcal/comm_hgcal/bainbrid/Photons/samples/FineCalo/220406/step3 --PtEta=pt${pT}_eta${eta} -G; done; done

# Status:
# condor_tail -f -stderr 2835402.99
