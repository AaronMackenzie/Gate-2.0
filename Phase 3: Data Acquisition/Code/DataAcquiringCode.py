import yfinance as yf
import pandas as pd
import time


start_time = time.time()


# Define asset symbols
assets = [
    # Precious Metals
    "XAUUSD=X", "XAGUSD=X", "PL=F", "PA=F", "GLD", "IAU", "PHYS", "SLV", "SIVR", "GOLD", "NEM",  

    # Energy Commodities
    "NG=F", "LNG", "UXC", "RB=F", "BZ=F", "CL=F", "HO=F",  

    # Agricultural Commodities
    "ZW=F", "ZC=F", "ZR=F", "ZS=F", "ZB=F", "ZO=F", "SB=F", "CC=F", "CT=F", "PALM",  

    # Industrial & Base Metals
    "HG=F", "ALI=F", "NICKEL", "ZNC=F", "TIN", "LEAD", "COBALT", "LIT", "TITANIUM",  

    # Livestock & Meat
    "LE=F", "GF=F", "HE=F", "CHICKEN", "MILK",  

    # Soft Commodities
    "TEA", "RUBBER", "HONEY",  

    # Commodity ETFs & Index Funds
    "GLD", "SLV", "UNG", "DBC", "ICLN", "FIW", "DBA", "JJM",
    
     "AAPL", "MSFT", "JNJ", "PG", "KO", "PEP", "WMT", "NSRGY", "UL", "BRK-B",  # Blue-Chip Stocks
    "MCD", "CL", "MMM", "ABBV", "T", "VZ", "CAT", "IBM", "HD", "MDT",  # Dividend Aristocrats
    "PFE", "MRK", "KMB", "DUK", "SO", "AWK", "WM", "GIS", "KHC", "CLX",  # Defensive Sector Stocks
    "SPY", "VIG", "USMV", "SPLV", "DVY", "VDC", "VPU", "SCHD", "IYH", "FDLO",  # Stable ETFs
    "O", "AMT", "PSA", "EQIX", "PLD", "AVB", "VTR", "SPG", "WELL", "CCI",  # REITs
    
    
    
   # 1️⃣ Stablecoins (Fiat-Pegged & Low Volatility)
    "USDT-USD", "USDC-USD", "BUSD-USD", "DAI-USD", "TUSD-USD", "USDP-USD", "USTC-USD", "GUSD-USD", "LUSD-USD", 
    "RSV-USD", "HUSD-USD", "USDS-USD", 

    # 2️⃣ Major Cryptocurrencies
    "BTC-USD", "ETH-USD", "BNB-USD", "XRP-USD", "ADA-USD", "DOT-USD", "SOL-USD", "LTC-USD", "AVAX-USD", "LINK-USD",

    # 3️⃣ Asset-Backed Cryptos
    "PAXG-USD", "XAUT-USD", "DGX-USD", "PMGT-USD", "AWG-USD", "AWS-USD", "sXAU-USD",

    # 4️⃣ Central Bank Digital Currencies (CBDCs) - Proxies via Forex
    "CNY=X",  # Digital Yuan
    "EUR=X",  # Digital Euro
    "SEK=X",  # e-Krona proxy
    "BSD=X",  # Sand Dollar (proxy via Bahamian Dollar)
    
    # 5️⃣ Utility Tokens & Exchange Coins
    "UNI-USD", "OKB-USD", "FTT-USD", "CRO-USD", "KCS-USD", "HT-USD", "BTT-USD", "MKR-USD",
    
     "^IRX", "^FVX", "^TNX", "^TYX",  # US T-Bills, T-Notes, T-Bonds (1M, 5Y, 10Y, 30Y yields)
    "TLT", "IEI", "SHY", "IEF", "BIL",  # US Treasury ETFs
    "VGIT", "SCHO", "SPTL", "SCHR", "GOVT",  # More Treasury ETFs
    "UK10Y=GB", "DE10Y=DE", "JP10Y=JP", "CA10Y=CA", "AU10Y=AU", "CH10Y=CH",  # 10-year bonds from UK, Germany, Japan, Canada, Australia, Switzerland

    # Municipal Bonds
    "MUB", "TFI", "VTEB", "SUB",  # Municipal Bond ETFs
    "FTABX",  # Fidelity Municipal Bond Fund

    # Corporate Bonds
    "LQD", "VCIT", "VCSH", "IGIB", "IGSB",  # Investment-Grade Corporate Bonds ETFs
    "HYG", "JNK", "SJNK", "ANGL",  # High-Yield (Junk) Bond ETFs
    "EMB", "VWOB",  # Emerging Market Bond ETFs
    "BND", "AGG", "SCHZ", "BNDX",  # Aggregate Bond Market ETFs

    # Inflation-Protected Bonds (TIPS)
    "TIP", "VTIP", "SCHP", "LTPZ", "TDTT",  # TIPS Bond ETFs
    
    
    
     # 1️⃣ Direct Property Ownership (Physical Real Estate) - Proxies where available
    "PLD", "O", "AVB", "EQR", "MAA", "CPT", "ELS", "EXR", "PSA", "IRM", "DLR", "EQIX",
    
    # 2️⃣ Real Estate Investment Trusts (REITs)
    "VTR", "WELL", "DOC", "MPW", "NHI", "REG", "FRT", "SPG", "CCI", "AMT", "SBAC", "INVH", "UDR", "EQR", "STAG", "PLD", "COLD", "LAND", "FPI", "WY", "PCH", "TRNO",
    
    # 3️⃣ Mortgage-Backed Securities (MBS) & Debt-Based Real Estate Assets
    "AGNC", "NLY", "STWD", "BXMT", "ABR", "LADR", "RITM", "CIM", "SACH", "RC",
    
    # 4️⃣ Tokenized Real Estate & Digital Assets - Limited availability on Yahoo Finance
    "BTG", "GDL", "RA",
    
    # 5️⃣ Real Estate Crowdfunding & Alternative Investments
    "VNQ", "SCHH", "IYR", "REET", "REM", "RWO", "KBWY", "FREL", "ROOF",
    
    
     # 1️⃣ Collectibles (Tangible & Historical Assets)
    "SOTHEBY",
    "CHRISTIES",
    "RMBS",
    "PPRUF",
    "MC.PA",
    "CFRUY",
    "BRBY.L",
    "LVMUY",
    "STZ",
    "BF-B",
    "DIS",
    "NFLX",
    "MAR",
    "RL",
    "PATEK",
    "PHIL",
    "VINTAGE",
    
    # 2️⃣ Private Equity & Venture Capital (Stable Business Assets)
    "BX",
    "KKR",
    "CG",
    "APO",
    "ARES",
    "TPG",
    "OAK-A",
    "BRK-B",
    "BAM",
    "GSBD",
    
    # 3️⃣ Hedge Funds (Low-Volatility Strategies)
    "MANU",
    "PDT",
    "JHQAX",
    "MERFX",
    "ARBFX",
    "DBLTX",
    "PIMIX",
    "JHEQX",
    "PGAFX",
    "QRHAX",
    
    # 4️⃣ Infrastructure & Hard Assets
    "BIP",
    "BEPC",
    "NEE",
    "DUK",
    "VZ",
    "AMT",
    "CCI",
    "CSX",
    "NSC",
    "UNP",
    "FPI",
    "LAND",
    "WY",
    "PCH",
    
    # 5️⃣ Digital Alternative Assets (Stable Non-Crypto Options)
    "EIGI",
    "TSQ",
    "SONG",
    "DIS",
    "WMG",
    "RPMT",
    "RBLX",
    "ESEA",
    "META",
    "U",
    
    
    
     # 1️⃣ Interest Rate Derivatives (Lower Volatility)
    "^IRX", "^FVX", "^TNX", "^TYX", "ZB=F", "ZN=F", "ZF=F", "ZT=F",
    
    # 2️⃣ Low-Volatility Commodity Derivatives
    "GC=F", "SI=F", "ZW=F", "ZC=F", "ZS=F", "LE=F", "GF=F", "CC=F", "KC=F", "CT=F", "LB=F", "DA=F", "OJ=F",
    
    # 3️⃣ Currency Derivatives (Lower Volatility FX Contracts)
    "DX-Y.NYB", "6E=F", "6J=F", "CNH=X", "EURUSD=X", "USDJPY=X", "USDCNH=X",
    
    # 4️⃣ Equity Derivatives (Low-Volatility Stock Market Contracts)
    "ES=F", "YM=F", "VX=F", "SPY", "DIA", "SPLV", "VIXM",
    
    # 5️⃣ Structured & Exotic Derivatives (Stability-Focused Instruments)
    "LQD", "HYG", "TIP", "BND", "AGG", "CDS=F"
    
    
    
    
]

# Define timeframes and max historical data allowed
intervals = {
    "1m": "8d",
    "2m": "60d",
    "5m": "60d",
    "15m": "60d",
    "30m": "60d",
    "1h": "730d",
    "4h": "730d",
    "1d": "max",
    "1wk": "max",
    "1mo": "max"
}

# Loop through each asset and download data
for asset in assets:
    for interval, period in intervals.items():
        try:
            time.sleep(1)
            print(f"Downloading {asset} data for {interval} timeframe...")
            data = yf.download(asset, interval=interval, period=period)
            if not data.empty:
                filename = f"{asset.replace('=F', '').replace('=X', '')}_{interval}.csv"
                data.to_csv(filename)
                print(f"Saved: {filename}")
            else:
                print(f"No data available for {asset} at {interval} timeframe.")
        except Exception as e:
            print(f"Error downloading {asset} at {interval}: {e}")

print("Data download complete.")
print("Time taken:", time.time() - start_time, "seconds")






