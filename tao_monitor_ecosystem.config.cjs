module.exports = {
  apps: [
    {
      name: "tao-monitor",
      script: "/Users/lewisjackson/Desktop/TAO_WALLET/tao_monitor.py",
      interpreter: "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3",
      cron_restart: "0 * * * *",   // every hour on the hour
      autorestart: false,
      watch: false,
      out_file: "/Users/lewisjackson/Desktop/TAO_WALLET/tao_monitor.log",
      error_file: "/Users/lewisjackson/Desktop/TAO_WALLET/tao_monitor_err.log",
    },
  ],
};
