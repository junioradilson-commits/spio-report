"""
╔══════════════════════════════════════════════════════════════════╗
║  WHATSAPP REPORT — REGIONAL SPIO · MERCADO LIVRE ENVIOS 2026    ║
║  Design: Andes Design System · Paleta pastel · Mobile 520px     ║
║  Páginas: Last Mile (SSP*) + First Mile (BRXSP*)                ║
╚══════════════════════════════════════════════════════════════════╝
Rodando no Claude Code:
    cd C:\\Users\\adilsojunior\\Documents
    python whatsapp_spio_v2.py
    → Abre whatsapp_spio_v2.html no browser
    → Print da tela → enviar no grupo WhatsApp

Para conectar dados reais do BQ, substitua os blocos marcados com:
    # ⚠️ BQ REAL: <query>
"""
import warnings; warnings.filterwarnings("ignore")
import sys; sys.stdout.reconfigure(encoding="utf-8")
from datetime import date
import webbrowser, os

# ══════════════════════════════════════════════════════════
#  CONFIGURAÇÃO DE PERÍODO
# ══════════════════════════════════════════════════════════
SEMANA_ATUAL = "10/04 – 17/04/2026"
DATA_GERACAO = date.today().strftime("%d/%m/%Y")

# ══════════════════════════════════════════════════════════
#  ANDES DESIGN SYSTEM — MERCADO LIVRE
#  Cores primárias: #FFE600 (Turbo Yellow) + #2D3277 (Astronaut Blue)
#  Paleta pastel para relatórios de dados
# ══════════════════════════════════════════════════════════
STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
*{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased}
.wb{max-width:520px;margin:0 auto;font-family:'Nunito',system-ui,sans-serif;background:#F7F6F0}
.hdr{background:#FFE600;padding:18px 20px 20px;position:relative;overflow:hidden}
.hc1{position:absolute;top:-28px;right:-28px;width:120px;height:120px;border-radius:50%;background:rgba(45,50,119,.10)}
.hc2{position:absolute;bottom:-20px;right:48px;width:70px;height:70px;border-radius:50%;background:rgba(45,50,119,.07)}
.hbadge{display:inline-block;background:rgba(45,50,119,.13);border-radius:20px;padding:3px 11px;font-size:10px;font-weight:700;color:#1A237E;letter-spacing:1.2px;margin-bottom:10px}
.htitle{font-size:22px;font-weight:900;color:#212121;line-height:1.2;margin-bottom:3px}
.hsub{font-size:11px;color:#424242;opacity:.65;margin-bottom:10px}
.hweek{display:inline-block;background:#2D3277;color:#FFE600;font-size:10px;font-weight:700;padding:4px 12px;border-radius:20px;letter-spacing:.5px}
.nav-wrap{background:#2D3277;padding:12px 14px;display:flex;gap:10px}
.nav-tab{flex:1;padding:10px 12px;font-family:'Nunito',sans-serif;font-size:11px;font-weight:700;border:none;cursor:pointer;letter-spacing:.8px;text-transform:uppercase;transition:all .25s;display:flex;align-items:center;justify-content:center;gap:7px;border-radius:12px;color:rgba(255,255,255,.40);background:rgba(255,255,255,.08)}
.nav-tab:hover{background:rgba(255,255,255,.15);color:rgba(255,255,255,.70)}
.nav-tab.active-lm{background:#FFE600;color:#212121;box-shadow:0 2px 8px rgba(255,230,0,.35)}
.nav-tab.active-fm{background:#FFE600;color:#1A237E;box-shadow:0 2px 8px rgba(255,230,0,.35)}
.page{display:none}
.page.active{display:block}
.body{padding:14px}
.sbar{display:flex;align-items:center;gap:10px;padding:12px 16px}
.sdot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.sinfo{flex:1}
.stitle{font-size:12px;font-weight:700;letter-spacing:.3px}
.ssub{font-size:10px;opacity:.55;margin-top:1px}
.sbig{font-size:22px;font-weight:900}
.sec{background:#fff;border-radius:16px;padding:16px;margin-bottom:12px;border:0.5px solid rgba(0,0,0,.06)}
.shead{display:flex;align-items:center;gap:8px;margin-bottom:12px}
.sicon{font-size:14px;width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.stitleb{font-size:12px;font-weight:700;color:#424242;letter-spacing:.8px;text-transform:uppercase}
.clabel{font-size:10px;font-weight:700;color:#757575;letter-spacing:.8px;text-transform:uppercase;margin-bottom:8px}
.kgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:9px}
.kcard{border-radius:12px;padding:12px 13px;position:relative;overflow:hidden}
.klabel{font-size:9px;font-weight:700;color:rgba(0,0,0,.45);letter-spacing:1.3px;text-transform:uppercase;margin-bottom:3px}
.kvalue{font-size:26px;font-weight:900;line-height:1;margin-bottom:3px}
.kdelta{font-size:10px;font-weight:700}
.ksub{font-size:9px;color:rgba(0,0,0,.45);margin-top:1px}
.kbadge{display:inline-block;font-size:9px;font-weight:700;letter-spacing:.8px;padding:2px 7px;border-radius:8px;margin-bottom:4px}
.otbl{width:100%;border-collapse:collapse;font-size:11px}
.otbl th{font-size:9px;font-weight:700;color:#9E9E9E;letter-spacing:1px;text-transform:uppercase;padding:5px 8px;background:#FAFAFA}
.otbl td{padding:7px 8px;border-top:0.5px solid #F5F5F5;font-weight:600;color:#212121}
.otbl tr:hover td{background:#FFFDE6}
.spill{display:inline-block;border-radius:8px;padding:2px 7px;font-size:9px;font-weight:700}
.pill{display:inline-block;border-radius:20px;padding:3px 9px;font-size:10px;font-weight:700}
.footer{text-align:center;padding:14px;font-size:9px;color:#9E9E9E;background:#F7F6F0}
"""

# ══════════════════════════════════════════════════════════
#  DADOS LAST MILE — SSP* (Service Centers)
#  ⚠️ BQ REAL:
#  SELECT op.CIDADE, SUM(desp) as desp, SUM(ent) as ent,
#         SAFE_DIVIDE(SUM(ent),SUM(desp))*100 as dsr
#  FROM BT_SHP_SHIPMENTS_LAST_MILE lm
#  JOIN DEPARA_REGIONAL op ON lm.SHP_LG_FACILITY_ID = op.ID_CODIGO
#  WHERE UPPER(op.REGIONAL) LIKE '%SPI%'
#    AND UPPER(op.ID_CODIGO) LIKE 'SSP%'
#    AND lm.SHP_LG_INIT_DT_TZ BETWEEN DATE_SUB(CURRENT_DATE,7) AND CURRENT_DATE
#  GROUP BY 1 ORDER BY dsr ASC
# ══════════════════════════════════════════════════════════
LM_DATA = [
    {"n":"Franca",      "dsr":94.81,"ant":92.62,"fdds":91.2,"ftds":88.5,"rts":5.19,"csat":72,"score":90.9},
    {"n":"S.Carlos",    "dsr":95.51,"ant":96.68,"fdds":92.1,"ftds":89.9,"rts":4.49,"csat":74,"score":91.8},
    {"n":"Cps Virtual", "dsr":95.90,"ant":94.11,"fdds":93.5,"ftds":91.2,"rts":4.10,"csat":76,"score":92.7},
    {"n":"Marília",     "dsr":96.48,"ant":95.95,"fdds":94.2,"ftds":92.1,"rts":3.52,"csat":78,"score":93.5},
    {"n":"Rib.Preto",   "dsr":96.51,"ant":95.51,"fdds":94.8,"ftds":93.4,"rts":3.49,"csat":79,"score":93.9},
    {"n":"Campinas",    "dsr":96.81,"ant":96.53,"fdds":95.1,"ftds":93.8,"rts":3.19,"csat":80,"score":94.3},
    {"n":"P.Prudente",  "dsr":97.18,"ant":95.59,"fdds":95.9,"ftds":94.2,"rts":2.82,"csat":82,"score":95.0},
    {"n":"Jales",       "dsr":97.58,"ant":96.77,"fdds":96.3,"ftds":94.9,"rts":2.42,"csat":83,"score":95.5},
    {"n":"S.J.R.Preto", "dsr":97.71,"ant":97.39,"fdds":96.5,"ftds":95.1,"rts":2.29,"csat":84,"score":95.7},
    {"n":"Bauru",       "dsr":97.83,"ant":97.39,"fdds":96.8,"ftds":95.6,"rts":2.17,"csat":85,"score":96.0},
    {"n":"Araçatuba",   "dsr":98.27,"ant":96.99,"fdds":97.1,"ftds":96.2,"rts":1.73,"csat":87,"score":96.6},
    {"n":"Barretos",    "dsr":99.01,"ant":98.72,"fdds":97.8,"ftds":97.1,"rts":0.99,"csat":89,"score":97.5},
    {"n":"Avaré",       "dsr":99.17,"ant":98.59,"fdds":98.1,"ftds":97.5,"rts":0.83,"csat":90,"score":97.8},
]

# ══════════════════════════════════════════════════════════
#  DADOS FIRST MILE — BRXSP* (Hubs XD)
#  ⚠️ BQ REAL:
#  SELECT d.CIDADE, d.ID_CODIGO,
#         SAFE_DIVIDE(COUNTIF(PICKUP_SUCCESS=1),COUNT(*))*100 as pus,
#         COUNTIF(PICKUP_SUCCESS_CLASIFICATION IS NOT NULL) as est,
#         COUNTIF(PICKUP_SUCCESS=1) as col,
#         SAFE_DIVIDE(COUNTIF(PUS_D=1),COUNT(*))*100 as backlog
#  FROM DM_SHP_XD_PICKUP p
#  JOIN DEPARA_REGIONAL d ON p.HUB_ID = d.ID_CODIGO
#  WHERE UPPER(d.REGIONAL) LIKE '%SPI%'
#    AND UPPER(d.ID_CODIGO) LIKE 'BRXSP%'
#    AND DATE BETWEEN DATE_SUB(CURRENT_DATE,7) AND CURRENT_DATE
#  GROUP BY 1,2
# ══════════════════════════════════════════════════════════
FM_DATA = [
    {"n":"Campinas",   "id":"BRXSP2",  "pus":94.2,"pant":93.1,"cr":94.3,"bl":8.5, "ea":15.2,"cap":2.1,"drv":1.8,"car":0.9,"oth":1.0,"est":18500,"col":17427,"spr":68.5},
    {"n":"Franca",     "id":"BRXSP8",  "pus":91.8,"pant":90.5,"cr":92.0,"bl":12.3,"ea":18.6,"cap":3.5,"drv":2.9,"car":1.2,"oth":1.6,"est":12300,"col":11315,"spr":54.2},
    {"n":"Rib.Preto",  "id":"BRXSP5",  "pus":93.5,"pant":92.8,"cr":93.4,"bl":10.1,"ea":16.3,"cap":2.8,"drv":2.1,"car":1.0,"oth":0.6,"est":15800,"col":14763,"spr":62.8},
    {"n":"Bauru",      "id":"BRXSP7",  "pus":95.1,"pant":94.3,"cr":95.1,"bl":6.8, "ea":14.1,"cap":1.9,"drv":1.4,"car":0.7,"oth":0.8,"est":21200,"col":20161,"spr":71.3},
    {"n":"Marília",    "id":"BRXSP14", "pus":92.7,"pant":91.9,"cr":92.7,"bl":11.7,"ea":17.8,"cap":3.2,"drv":2.6,"car":1.1,"oth":0.7,"est":11900,"col":11033,"spr":57.4},
    {"n":"P.Prudente", "id":"BRXSP11", "pus":93.0,"pant":92.1,"cr":93.0,"bl":9.4, "ea":15.9,"cap":2.9,"drv":2.3,"car":0.9,"oth":0.9,"est":14600,"col":13578,"spr":60.1},
]

# ══════════════════════════════════════════════════════════
#  KPIs REGIONAIS CALCULADOS
# ══════════════════════════════════════════════════════════
lm_dsr   = 97.00
lm_ant   = 96.24
lm_wow   = round(lm_dsr - lm_ant, 2)
lm_desp  = 2373261
lm_ne    = 71186
lm_fdds  = round(sum(o["fdds"] for o in LM_DATA) / len(LM_DATA), 1)
lm_csat  = round(sum(o["csat"] for o in LM_DATA) / len(LM_DATA), 1)
lm_score = round(sum(o["score"] for o in LM_DATA) / len(LM_DATA), 1)
lm_crit  = [o["n"] for o in LM_DATA if o["dsr"] < 95]
lm_aten  = [o["n"] for o in LM_DATA if 95 <= o["dsr"] < 97]
lm_ok    = [o["n"] for o in LM_DATA if o["dsr"] >= 97]
lm_lider = max(LM_DATA, key=lambda x: x["score"])["n"]

fm_pus   = round(sum(o["pus"] for o in FM_DATA) / len(FM_DATA), 1)
fm_est   = sum(o["est"] for o in FM_DATA)
fm_col   = sum(o["col"] for o in FM_DATA)
fm_cr    = round(fm_col / fm_est * 100, 1)
fm_bl    = round(sum(o["bl"] for o in FM_DATA) / len(FM_DATA), 1)
fm_ok    = sum(1 for o in FM_DATA if o["pus"] >= 94)
fm_lider = max(FM_DATA, key=lambda x: x["pus"])["n"]

# ══════════════════════════════════════════════════════════
#  JAVASCRIPT — Chart.js + lógica de navegação
# ══════════════════════════════════════════════════════════
import json
LM_JSON = json.dumps(LM_DATA)
FM_JSON = json.dumps(FM_DATA)

JS = f"""
Chart.register(ChartDataLabels);

function showPage(p,btn){{
  document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));
  document.querySelectorAll('.nav-tab').forEach(x=>{{x.classList.remove('active-lm','active-fm')}});
  document.getElementById('page-'+p).classList.add('active');
  btn.classList.add('active-'+p);
  window.scrollTo(0,0);
}}

const LM = {LM_JSON};
const FM = {FM_JSON};

function semC(v,low,mid){{
  if(v<low) return {{bar:'#EF9595',bdr:'#B71C1C',txt:'#B71C1C',bg:'#FFEBEE',lbl:'CRÍTICO'}};
  if(v<mid) return {{bar:'#FFCC80',bdr:'#E65100',txt:'#E65100',bg:'#FFF3E0',lbl:'ATENÇÃO'}};
  return {{bar:'#A5D6A7',bdr:'#2E7D32',txt:'#2E7D32',bg:'#E8F5E9',lbl:'OK'}};
}}
function semPUS(v){{return semC(v,92,94)}}
const MEDALS=['🥇','🥈','🥉'];

const bOpts={{responsive:true,maintainAspectRatio:false,
  plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>{{
    const v=Array.isArray(c.raw)?c.raw[1]:c.raw;
    return ' '+(c.dataset.label||'')+': '+v.toFixed(1)+'%';
  }}}}}}}}}};

/* ── LM TABLE ── */
const lmTb=document.getElementById('lm-tbody');
[...LM].sort((a,b)=>b.dsr-a.dsr).forEach(op=>{{
  const c=semC(op.dsr,95,97);
  const w=op.dsr-op.ant,wc=w>=0?'#2E7D32':'#C62828';
  lmTb.innerHTML+=`<tr>
    <td>${{op.n}}</td>
    <td style="text-align:center"><span class="spill" style="background:${{c.bg}};color:${{c.txt}}">${{op.dsr.toFixed(1)}}%</span></td>
    <td style="text-align:center;color:${{wc}};font-size:10px">${{w>=0?'▲':'▼'}}${{Math.abs(w).toFixed(2)}}pp</td>
    <td style="text-align:center"><span class="spill" style="background:${{c.bg}};color:${{c.txt}}">${{c.lbl}}</span></td>
  </tr>`;
}});

/* ── FM TABLE ── */
const fmTb=document.getElementById('fm-tbody');
[...FM].sort((a,b)=>b.pus-a.pus).forEach(op=>{{
  const c=semPUS(op.pus);
  const w=op.pus-op.pant,wc=w>=0?'#2E7D32':'#C62828';
  const blc=op.bl>=10?'#B71C1C':'#2E7D32';
  fmTb.innerHTML+=`<tr>
    <td>${{op.n}}<br><span style="font-size:9px;color:#9E9E9E">${{op.id}}</span></td>
    <td style="text-align:center"><span class="spill" style="background:${{c.bg}};color:${{c.txt}}">${{op.pus.toFixed(1)}}%</span></td>
    <td style="text-align:center;color:${{wc}};font-size:10px">${{w>=0?'▲':'▼'}}${{Math.abs(w).toFixed(2)}}pp</td>
    <td style="text-align:center;font-size:10px;font-weight:700;color:#1A237E">${{op.cr.toFixed(1)}}%</td>
    <td style="text-align:center;font-size:10px;font-weight:700;color:${{blc}}">${{op.bl.toFixed(1)}}%</td>
  </tr>`;
}});

/* ── CHART 1: DSR — FLOATING BARS [88, valor] ── */
const lmS=[...LM].sort((a,b)=>a.dsr-b.dsr);
const BASE=88;
new Chart(document.getElementById('cDSR'),{{
  type:'bar',
  data:{{labels:lmS.map(o=>o.n),datasets:[{{
    data:lmS.map(o=>[BASE,o.dsr]),
    backgroundColor:lmS.map(o=>semC(o.dsr,95,97).bar),
    borderColor:lmS.map(o=>semC(o.dsr,95,97).bdr),
    borderWidth:1,borderRadius:5,borderSkipped:false,
  }}]}},
  options:{{...bOpts,indexAxis:'y',
    scales:{{
      x:{{min:BASE,max:101,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{callback:v=>v+'%',font:{{size:10}}}}}},
      y:{{grid:{{display:false}},ticks:{{font:{{size:11,weight:'700'}}}}}}
    }},
    plugins:{{...bOpts.plugins,
      tooltip:{{callbacks:{{label:c=>{{const v=Array.isArray(c.raw)?c.raw[1]:c.raw;return ' DSR: '+v.toFixed(2)+'%'}}}}}},
      datalabels:{{
        display:true,
        anchor:'end', align:'end',
        formatter:(val)=>{{const v=Array.isArray(val)?val[1]:val;return v.toFixed(1)+'%'}},
        font:{{size:11,weight:'700',family:"'Nunito',sans-serif"}},
        color:'#424242',
        padding:{{left:4}}
      }}
    }}
  }}
}});

/* ── CHART 2: WoW — FLOATING BARS agrupadas ── */
const wS=[...LM].sort((a,b)=>a.dsr-b.dsr);
const WB=92;
new Chart(document.getElementById('cWoW'),{{
  type:'bar',
  data:{{labels:wS.map(o=>o.n),datasets:[
    {{label:'Anterior',data:wS.map(o=>[WB,o.ant]),backgroundColor:'rgba(189,189,189,0.35)',borderColor:'rgba(158,158,158,0.6)',borderWidth:1,borderRadius:3,borderSkipped:false,barPercentage:0.4,categoryPercentage:0.8,
      datalabels:{{display:false}}}},
    {{label:'Atual',data:wS.map(o=>[WB,o.dsr]),backgroundColor:wS.map(o=>semC(o.dsr,95,97).bar),borderColor:wS.map(o=>semC(o.dsr,95,97).bdr),borderWidth:1.5,borderRadius:5,borderSkipped:false,barPercentage:0.6,categoryPercentage:0.8,
      datalabels:{{
        display:true,anchor:'end',align:'end',
        formatter:(val)=>{{const v=Array.isArray(val)?val[1]:val;return v.toFixed(1)+'%'}},
        font:{{size:10,weight:'700',family:"'Nunito',sans-serif"}},color:'#424242',padding:{{left:3}}
      }}}},
  ]}},
  options:{{...bOpts,indexAxis:'y',
    scales:{{
      x:{{min:WB,max:101,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{callback:v=>v+'%',font:{{size:10}}}}}},
      y:{{grid:{{display:false}},ticks:{{font:{{size:11,weight:'700'}}}}}}
    }},
    plugins:{{...bOpts.plugins,legend:{{display:true,position:'bottom',labels:{{font:{{size:10}},boxWidth:10,padding:8}}}},
      datalabels:{{display:false}}
    }}
  }}
}});

/* ── CHART 3: RANKING — FLOATING BARS ── */
const rS=[...LM].sort((a,b)=>b.score-a.score);
const RB=87;
new Chart(document.getElementById('cRank'),{{
  type:'bar',
  data:{{labels:rS.map((o,i)=>(MEDALS[i]||'')+' '+o.n),datasets:[{{
    data:rS.map(o=>[RB,o.score]),
    backgroundColor:rS.map(o=>semC(o.dsr,95,97).bar),
    borderColor:rS.map(o=>semC(o.dsr,95,97).bdr),
    borderWidth:1,borderRadius:5,borderSkipped:false,
  }}]}},
  options:{{...bOpts,indexAxis:'y',
    scales:{{
      x:{{min:RB,max:100,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{font:{{size:10}}}}}},
      y:{{grid:{{display:false}},ticks:{{font:{{size:11,weight:'700'}}}}}}
    }},
    plugins:{{...bOpts.plugins,
      tooltip:{{callbacks:{{label:c=>{{const v=Array.isArray(c.raw)?c.raw[1]:c.raw;return ' Score: '+v.toFixed(1)}}}}}},
      datalabels:{{
        display:true,anchor:'end',align:'end',
        formatter:(val)=>{{const v=Array.isArray(val)?val[1]:val;return v.toFixed(1)}},
        font:{{size:11,weight:'700',family:"'Nunito',sans-serif"}},color:'#424242',padding:{{left:4}}
      }}
    }}
  }}
}});

/* ── HEATMAP LM ── */
const KPIS=['DSR','FDDS','FTDS','CSAT','Anti-RTS'];
const gV=(op,k)=>k==='DSR'?op.dsr:k==='FDDS'?op.fdds:k==='FTDS'?op.ftds:k==='CSAT'?op.csat:100-op.rts;
const mn={{}},mx={{}};
KPIS.forEach(k=>{{const v=LM.map(o=>gV(o,k));mn[k]=Math.min(...v);mx[k]=Math.max(...v);}});
function hc(v,a,b){{const t=(v-a)/(b-a+.001);return `rgb(${{Math.round(255-t*55)}},${{Math.round(215+t*40)}},${{Math.round(215-t*90)}})`;}}
const hmLM=document.getElementById('hmLM');
hmLM.innerHTML='<tr><th style="padding:5px 6px;font-size:9px;color:#9E9E9E;background:#FAFAFA;text-align:left">Op.</th>'+
  KPIS.map(k=>`<th style="padding:5px 4px;font-size:9px;color:#9E9E9E;background:#FAFAFA;text-align:center">${{k}}</th>`).join('')+'</tr>';
[...LM].sort((a,b)=>b.dsr-a.dsr).forEach(op=>{{
  hmLM.innerHTML+=`<tr><td style="padding:5px 6px;font-size:10px;font-weight:600;color:#424242;white-space:nowrap">${{op.n}}</td>`+
  KPIS.map(k=>{{const v=gV(op,k);return `<td style="padding:5px 4px;text-align:center;background:${{hc(v,mn[k],mx[k])}};font-size:10px;font-weight:700;color:#424242">${{v.toFixed(1)}}%</td>`;}}).join('')+'</tr>';
}});

/* ── FM CHART 1: PUS ── */
const PB=85;
new Chart(document.getElementById('cPUS'),{{
  type:'bar',
  data:{{labels:FM.map(o=>o.n),datasets:[
    {{label:'Anterior',data:FM.map(o=>[PB,o.pant]),backgroundColor:'rgba(189,189,189,0.35)',borderColor:'rgba(158,158,158,0.6)',borderWidth:1,borderRadius:3,borderSkipped:false,barPercentage:0.4,categoryPercentage:0.9,
      datalabels:{{
        display:true,anchor:'end',align:'top',
        formatter:(val)=>{{const v=Array.isArray(val)?val[1]:val;return v.toFixed(1)+'%'}},
        font:{{size:10,weight:'600',family:"'Nunito',sans-serif"}},color:'#9E9E9E',padding:{{bottom:2}}
      }}}},
    {{label:'Atual',data:FM.map(o=>[PB,o.pus]),backgroundColor:FM.map(o=>semPUS(o.pus).bar),borderColor:FM.map(o=>semPUS(o.pus).bdr),borderWidth:1.5,borderRadius:5,borderSkipped:false,barPercentage:0.6,categoryPercentage:0.9,
      datalabels:{{
        display:true,anchor:'end',align:'top',
        formatter:(val)=>{{const v=Array.isArray(val)?val[1]:val;return v.toFixed(1)+'%'}},
        font:{{size:11,weight:'700',family:"'Nunito',sans-serif"}},color:'#424242',padding:{{bottom:3}}
      }}}},
  ]}},
  options:{{...bOpts,
    scales:{{
      x:{{ticks:{{font:{{size:11,weight:'700'}}}},grid:{{display:false}}}},
      y:{{min:PB,max:99,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{callback:v=>v+'%',font:{{size:10}}}}}}
    }},
    plugins:{{...bOpts.plugins,legend:{{display:true,position:'bottom',labels:{{font:{{size:10}},boxWidth:10,padding:8}}}},
      datalabels:{{display:false}}
    }}
  }}
}});

/* ── FM CHART 2: No PUS ── */
new Chart(document.getElementById('cNoPUS'),{{
  type:'bar',
  data:{{labels:FM.map(o=>o.n),datasets:[
    {{label:'NS Capacity',data:FM.map(o=>o.cap),backgroundColor:'rgba(239,149,149,0.85)',borderColor:'#B71C1C',borderWidth:0.5,
      datalabels:{{formatter:v=>v>=0.5?v.toFixed(1)+'%':'',color:'#7f1010',font:{{size:10,weight:'700'}},anchor:'center',align:'center'}}}},
    {{label:'NS Driver',  data:FM.map(o=>o.drv),backgroundColor:'rgba(255,204,128,0.85)',borderColor:'#E65100',borderWidth:0.5,
      datalabels:{{formatter:v=>v>=0.5?v.toFixed(1)+'%':'',color:'#6d2800',font:{{size:10,weight:'700'}},anchor:'center',align:'center'}}}},
    {{label:'NS Carrier', data:FM.map(o=>o.car),backgroundColor:'rgba(249,168,37,0.7)', borderColor:'#F57F17',borderWidth:0.5,
      datalabels:{{formatter:v=>v>=0.4?v.toFixed(1)+'%':'',color:'#5c3900',font:{{size:10,weight:'700'}},anchor:'center',align:'center'}}}},
    {{label:'Outros',     data:FM.map(o=>o.oth),backgroundColor:'rgba(189,189,189,0.5)', borderColor:'#757575',borderWidth:0.5,
      datalabels:{{formatter:v=>v>=0.5?v.toFixed(1)+'%':'',color:'#424242',font:{{size:10,weight:'700'}},anchor:'center',align:'center'}}}},
  ]}},
  options:{{...bOpts,
    scales:{{
      x:{{ticks:{{font:{{size:11,weight:'700'}}}},grid:{{display:false}},stacked:true}},
      y:{{stacked:true,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{callback:v=>v+'%',font:{{size:10}}}}}}
    }},
    plugins:{{...bOpts.plugins,legend:{{display:true,position:'bottom',labels:{{font:{{size:10}},boxWidth:10,padding:6}}}},
      tooltip:{{callbacks:{{label:c=>` ${{c.dataset.label}}: ${{c.raw.toFixed(1)}}%`}}}},
      datalabels:{{display:true}}
    }}
  }}
}});

/* ── FM CHART 3: VOLUME ── */
new Chart(document.getElementById('cVol'),{{
  type:'bar',
  data:{{labels:FM.map(o=>o.n),datasets:[
    {{label:'Estimado',data:FM.map(o=>o.est),backgroundColor:'rgba(189,189,189,0.4)',borderColor:'rgba(158,158,158,0.6)',borderWidth:1,borderRadius:4,borderSkipped:false,order:2,yAxisID:'y',
      datalabels:{{display:true,anchor:'end',align:'top',formatter:v=>(v/1000).toFixed(1)+'K',font:{{size:9,weight:'600'}},color:'#757575',padding:{{bottom:2}}}}}},
    {{label:'Coletado', data:FM.map(o=>o.col),backgroundColor:FM.map(o=>semPUS(o.pus).bar),borderColor:FM.map(o=>semPUS(o.pus).bdr),borderWidth:1,borderRadius:4,borderSkipped:false,order:2,yAxisID:'y',
      datalabels:{{display:true,anchor:'end',align:'top',formatter:v=>(v/1000).toFixed(1)+'K',font:{{size:10,weight:'700'}},color:'#424242',padding:{{bottom:2}}}}}},
    {{label:'Collection Rate',data:FM.map(o=>parseFloat(o.cr.toFixed(1))),type:'line',borderColor:'#1A237E',backgroundColor:'rgba(26,35,126,0.1)',borderWidth:2,pointRadius:5,pointBackgroundColor:'#1A237E',order:1,yAxisID:'y2',tension:0.3,
      datalabels:{{display:true,anchor:'top',align:'top',formatter:v=>v.toFixed(1)+'%',font:{{size:10,weight:'700'}},color:'#1A237E',padding:{{bottom:3}}}}}},
  ]}},
  options:{{...bOpts,
    scales:{{
      x:{{ticks:{{font:{{size:11,weight:'700'}}}},grid:{{display:false}}}},
      y:{{grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{font:{{size:10}}}}}},
      y2:{{position:'right',min:88,max:100,grid:{{display:false}},ticks:{{callback:v=>v+'%',font:{{size:10}},color:'#1A237E'}}}},
    }},
    plugins:{{...bOpts.plugins,legend:{{display:true,position:'bottom',labels:{{font:{{size:10}},boxWidth:10,padding:8}}}},
      tooltip:{{callbacks:{{label:c=>{{const v=c.raw;return ` ${{c.dataset.label}}: ${{typeof v==='number'&&v>100?v.toLocaleString():v.toFixed(1)+'%'}}`}}}}}},
      datalabels:{{display:false}}
    }}
  }}
}});

/* ── FM CHART 4: BACKLOG vs EARLIES ── */
new Chart(document.getElementById('cBL'),{{
  type:'bar',
  data:{{labels:FM.map(o=>o.n),datasets:[
    {{label:'Backlog (EDPU vencida)',data:FM.map(o=>o.bl),backgroundColor:'rgba(239,149,149,0.75)',borderColor:'#B71C1C',borderWidth:1,borderRadius:4,borderSkipped:false,
      datalabels:{{display:true,anchor:'end',align:'top',formatter:v=>v.toFixed(1)+'%',font:{{size:11,weight:'700'}},color:'#B71C1C',padding:{{bottom:2}}}}}},
    {{label:'Earlies (EDPU futura)', data:FM.map(o=>o.ea),backgroundColor:'rgba(100,149,237,0.55)',borderColor:'#1A237E',borderWidth:1,borderRadius:4,borderSkipped:false,
      datalabels:{{display:true,anchor:'end',align:'top',formatter:v=>v.toFixed(1)+'%',font:{{size:11,weight:'700'}},color:'#1A237E',padding:{{bottom:2}}}}}},
  ]}},
  options:{{...bOpts,
    scales:{{
      x:{{ticks:{{font:{{size:11,weight:'700'}}}},grid:{{display:false}}}},
      y:{{max:25,grid:{{color:'rgba(0,0,0,.05)'}},ticks:{{callback:v=>v+'%',font:{{size:10}}}}}}
    }},
    plugins:{{...bOpts.plugins,legend:{{display:true,position:'bottom',labels:{{font:{{size:10}},boxWidth:10,padding:8}}}},
      tooltip:{{callbacks:{{label:c=>` ${{c.dataset.label}}: ${{c.raw.toFixed(1)}}%`}}}},
      datalabels:{{display:false}}
    }}
  }}
}});
"""

# ══════════════════════════════════════════════════════════
#  STATUS BAR LM
# ══════════════════════════════════════════════════════════
lm_status_dot   = "#66BB6A" if lm_dsr >= 97 else ("#FFA726" if lm_dsr >= 95 else "#EF5350")
lm_status_txt   = f"SPIO NO GREEN · DSR {lm_dsr:.2f}% · {'▲' if lm_wow>=0 else '▼'}{abs(lm_wow):.2f} p.p. WoW" if lm_dsr>=97 else f"ATENÇÃO · DSR {lm_dsr:.2f}%"
lm_crit_txt     = f"{len(lm_crit)} crítica(s) · {len(lm_aten)} em atenção · {len(lm_ok)} no verde · 13 service centers"

fm_pus_ok       = fm_pus >= 94
fm_status_txt   = f"{fm_ok} DE 6 HUBS NO GREEN · PUS MÉDIO {fm_pus:.1f}%"
fm_crit_ids     = [o["id"] for o in FM_DATA if o["pus"] < 92]
fm_aten_ids     = [o["id"] for o in FM_DATA if 92 <= o["pus"] < 94]

# ══════════════════════════════════════════════════════════
#  TEMPLATE HTML FINAL
# ══════════════════════════════════════════════════════════
HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0">
<title>SPIO Weekly Report | Mercado Livre DX</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-datalabels/2.2.0/chartjs-plugin-datalabels.min.js"></script>
<style>{STYLES}</style>
</head>
<body>
<div class="wb">

<!-- HEADER -->
<div class="hdr">
  <div class="hc1"></div><div class="hc2"></div>
  <div class="hbadge">DRIVER EXPERIENCE · REGIONAL SPIO</div>
  <div class="htitle">Weekly Report<br>Regional SPIO</div>
  <div class="hsub">mercado livre · envios</div>
  <div class="hweek">📅 Semana {SEMANA_ATUAL}</div>
</div>

<!-- NAV TABS -->
<div class="nav-wrap">
  <button class="nav-tab active-lm" onclick="showPage('lm',this)" id="tab-lm">🚚 Last Mile</button>
  <div class="nav-divider"></div>
  <button class="nav-tab" onclick="showPage('fm',this)" id="tab-fm">📦 First Mile</button>
</div>

<!-- ════════════ LAST MILE ════════════ -->
<div class="page active" id="page-lm">

<div class="sbar" style="background:#2D3277">
  <div class="sdot" style="background:{lm_status_dot}"></div>
  <div class="sinfo">
    <div class="stitle" style="color:#FFE600">{lm_status_txt}</div>
    <div class="ssub" style="color:#fff">{lm_crit_txt}</div>
  </div>
  <div class="sbig" style="color:#fff">{lm_dsr:.0f}%</div>
</div>

<div class="body">

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFF9C4">📊</div><span class="stitleb">KPIs Regionais — Last Mile</span></div>
  <div class="kgrid">
    <div class="kcard" style="background:#FFFDE6">
      <div class="kbadge" style="background:#2D3277;color:#FFE600">DSR</div>
      <div class="klabel">Regional SPIO</div>
      <div class="kvalue" style="color:{'#2E7D32' if lm_dsr>=97 else '#E65100'}">{lm_dsr:.2f}%</div>
      <div class="kdelta" style="color:{'#2E7D32' if lm_wow>=0 else '#C62828'}">{'▲' if lm_wow>=0 else '▼'} {abs(lm_wow):.2f} p.p. WoW</div>
      <div class="ksub">Ref: {lm_ant:.2f}%</div>
    </div>
    <div class="kcard" style="background:#E8EAF6">
      <div class="kbadge" style="background:#1A237E;color:#fff">VOLUME</div>
      <div class="klabel">Despachado</div>
      <div class="kvalue" style="color:#1A237E">{lm_desp/1e6:.2f}M</div>
      <div class="kdelta" style="color:#2E7D32">▲ pacotes/semana</div>
      <div class="ksub">13 SVCs · SSP*</div>
    </div>
    <div class="kcard" style="background:#FFEBEE">
      <div class="klabel">Não Entregues</div>
      <div class="kvalue" style="color:#C62828">{lm_ne/1000:.1f}K</div>
      <div class="kdelta" style="color:#C62828">▼ {lm_ne/lm_desp*100:.2f}% do vol.</div>
      <div class="ksub">falhas na semana</div>
    </div>
    <div class="kcard" style="background:#E8F5E9">
      <div class="klabel">FDDS — 1º Dia</div>
      <div class="kvalue" style="color:#2E7D32;font-size:22px">{lm_fdds:.1f}%</div>
      <div class="kdelta" style="color:#2E7D32">▲ First Day Delivery</div>
      <div class="ksub">1º dia na rota</div>
    </div>
    <div class="kcard" style="background:#E8F5E9">
      <div class="klabel">Score Médio</div>
      <div class="kvalue" style="color:#2E7D32;font-size:22px">{lm_score:.1f}</div>
      <div class="kdelta" style="color:#2E7D32">▲ Líder: {lm_lider}</div>
      <div class="ksub">índice composto 6 KPIs</div>
    </div>
    <div class="kcard" style="background:#E8EAF6">
      <div class="klabel">CSAT Regional</div>
      <div class="kvalue" style="color:#1A237E;font-size:22px">{lm_csat:.0f}%</div>
      <div class="kdelta" style="color:{'#2E7D32' if lm_csat>=80 else '#E65100'}">{'▲' if lm_csat>=80 else '▼'} Driver Experience</div>
      <div class="ksub">satisfação motoristas</div>
    </div>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFEBEE">🚦</div><span class="stitleb">Status por Operação</span></div>
  <table class="otbl">
    <thead><tr>
      <th style="text-align:left">Operação</th>
      <th style="text-align:center">DSR</th>
      <th style="text-align:center">WoW</th>
      <th style="text-align:center">Status</th>
    </tr></thead>
    <tbody id="lm-tbody"></tbody>
  </table>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFFDE6">📦</div><span class="stitleb">DSR por Service Center</span></div>
  <div class="clabel">barras começam em 88% — diferença real visível — meta 97%</div>
  <div style="position:relative;width:100%;height:420px">
    <canvas id="cDSR" role="img" aria-label="DSR por service center ordenado por performance">DSR por SVC da SPIO</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#E8EAF6">🎯</div><span class="stitleb">WoW — Atual vs Anterior</span></div>
  <div class="clabel">cinza = semana anterior · colorido = semana atual</div>
  <div style="position:relative;width:100%;height:420px">
    <canvas id="cWoW" role="img" aria-label="Variação WoW de DSR por operação">WoW DSR SPIO</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#E8F5E9">🏆</div><span class="stitleb">Ranking — Score Composto</span></div>
  <div class="clabel">DSR·35% + FDDS·20% + FTDS·15% + Anti-RTS·10% + CSAT·10%</div>
  <div style="position:relative;width:100%;height:420px">
    <canvas id="cRank" role="img" aria-label="Ranking de score composto das operações">Ranking SPIO</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFF3E0">🗺️</div><span class="stitleb">Mapa de Calor — 5 KPIs</span></div>
  <div class="clabel">verde = melhor · vermelho pastel = atenção</div>
  <div style="overflow-x:auto"><table id="hmLM" style="width:100%;border-collapse:collapse;font-size:10px;min-width:340px"></table></div>
</div>

</div><!-- /body LM -->
</div><!-- /page-lm -->

<!-- ════════════ FIRST MILE ════════════ -->
<div class="page" id="page-fm">

<div class="sbar" style="background:#1A237E">
  <div class="sdot" style="background:{'#66BB6A' if fm_ok>=5 else '#FFA726'}"></div>
  <div class="sinfo">
    <div class="stitle" style="color:#C5CAE9">{fm_status_txt}</div>
    <div class="ssub" style="color:rgba(255,255,255,.5)">BRXSP* · Coleta de sellers · First Mile SPIO</div>
  </div>
  <div class="sbig" style="color:#C5CAE9">FM</div>
</div>

<div class="body">

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#E8EAF6">📊</div><span class="stitleb">KPIs Regionais — First Mile</span></div>
  <div class="kgrid">
    <div class="kcard" style="background:#E8EAF6">
      <div class="kbadge" style="background:#1A237E;color:#C5CAE9">PUS</div>
      <div class="klabel">Pick Up Success</div>
      <div class="kvalue" style="color:{'#2E7D32' if fm_pus>=94 else '#E65100'};font-size:22px">{fm_pus:.1f}%</div>
      <div class="kdelta" style="color:{'#2E7D32' if fm_pus>=94 else '#E65100'}">{'▲ acima' if fm_pus>=94 else '▼ abaixo'} da meta 94%</div>
      <div class="ksub">média 6 hubs XD</div>
    </div>
    <div class="kcard" style="background:#E8F5E9">
      <div class="klabel">Collection Rate</div>
      <div class="kvalue" style="color:#2E7D32;font-size:22px">{fm_cr:.1f}%</div>
      <div class="kdelta" style="color:#2E7D32">▲ coletado/estimado</div>
      <div class="ksub">6 hubs XD SPIO</div>
    </div>
    <div class="kcard" style="background:#E8EAF6">
      <div class="klabel">Shps Estimados</div>
      <div class="kvalue" style="color:#1A237E;font-size:20px">{fm_est/1000:.1f}K</div>
      <div class="kdelta" style="color:#1A237E">▲ a coletar/semana</div>
      <div class="ksub">6 hubs BRXSP*</div>
    </div>
    <div class="kcard" style="background:{'#FFEBEE' if fm_bl>=10 else '#E8F5E9'}">
      <div class="klabel">Backlog Médio</div>
      <div class="kvalue" style="color:{'#C62828' if fm_bl>=10 else '#2E7D32'};font-size:22px">{fm_bl:.1f}%</div>
      <div class="kdelta" style="color:{'#C62828' if fm_bl>=10 else '#2E7D32'}">{'▼ acima' if fm_bl>=10 else '▲ dentro'} do threshold 10%</div>
      <div class="ksub">EDPU vencida</div>
    </div>
    <div class="kcard" style="background:#FFFDE6">
      <div class="klabel">SPR FM Médio</div>
      <div class="kvalue" style="color:#424242;font-size:22px">{sum(o['spr'] for o in FM_DATA)/len(FM_DATA):.1f}</div>
      <div class="kdelta" style="color:#2E7D32">▲ shps/rota FM</div>
      <div class="ksub">produtividade coleta</div>
    </div>
    <div class="kcard" style="background:#E8F5E9">
      <div class="klabel">Hubs no Green</div>
      <div class="kvalue" style="color:#2E7D32;font-size:22px">{fm_ok}/6</div>
      <div class="kdelta" style="color:#2E7D32">▲ PUS ≥ 94%</div>
      <div class="ksub">{fm_lider} lidera: {max(FM_DATA, key=lambda x: x['pus'])['pus']:.1f}%</div>
    </div>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFEBEE">🚦</div><span class="stitleb">Status por Hub XD</span></div>
  <table class="otbl">
    <thead><tr>
      <th style="text-align:left">Hub XD</th>
      <th style="text-align:center">PUS</th>
      <th style="text-align:center">WoW</th>
      <th style="text-align:center">Coleta</th>
      <th style="text-align:center">Backlog</th>
    </tr></thead>
    <tbody id="fm-tbody"></tbody>
  </table>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#E8EAF6">📦</div><span class="stitleb">PUS por Hub — Atual vs Anterior</span></div>
  <div class="clabel">barras começam em 85% · meta 94%</div>
  <div style="position:relative;width:100%;height:300px">
    <canvas id="cPUS" role="img" aria-label="PUS por hub XD atual vs anterior">PUS hubs SPIO</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFF3E0">❌</div><span class="stitleb">Motivos de Falha — No PUS</span></div>
  <div class="clabel">NS Capacity / Driver / Carrier / Outros</div>
  <div style="position:relative;width:100%;height:280px">
    <canvas id="cNoPUS" role="img" aria-label="Breakdown de motivos de falha na coleta">No PUS breakdown SPIO</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#FFFDE6">📊</div><span class="stitleb">Volume: Estimado vs Coletado</span></div>
  <div class="clabel">cinza = estimado · colorido = coletado · linha = taxa</div>
  <div style="position:relative;width:100%;height:280px">
    <canvas id="cVol" role="img" aria-label="Volume estimado vs coletado por hub">Volume FM hubs</canvas>
  </div>
</div>

<div class="sec">
  <div class="shead"><div class="sicon" style="background:#E8F5E9">⏱️</div><span class="stitleb">Backlog vs Earlies por Hub</span></div>
  <div class="clabel">backlog &gt; 10% = alerta · earlies = pacotes adiantados</div>
  <div style="position:relative;width:100%;height:280px">
    <canvas id="cBL" role="img" aria-label="Backlog e earlies por hub XD">Backlog Earlies SPIO</canvas>
  </div>
</div>

</div><!-- /body FM -->
</div><!-- /page-fm -->

<div class="footer">
  Fonte: BT_SHP_SHIPMENTS_LAST_MILE · DM_SHP_XD_PICKUP · DEPARA_REGIONAL<br>
  Mercado Livre · Driver Experience · SPIO · {DATA_GERACAO}
</div>

</div><!-- /wb -->

<script>
{JS}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════════════
#  SALVAR E ABRIR
# ══════════════════════════════════════════════════════════
OUTPUT = "whatsapp_spio_v2.html"
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"✅ WhatsApp Report gerado: {OUTPUT}")
print(f"   📱 Last Mile:  13 SVCs · DSR {lm_dsr}% · {len(lm_crit)} crítica(s)")
print(f"   📦 First Mile: 6 Hubs · PUS {fm_pus}% · {fm_ok}/6 no green")
print(f"   🎨 Design: Andes DS · Paleta pastel · Mobile 520px")
print(f"\n   Abrindo no browser...")

# Abrir automaticamente no browser
path = os.path.abspath(OUTPUT)
webbrowser.open(f"file:///{path}")
print(f"   → {path}")
