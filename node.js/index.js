#!/usr/bin/env node
/**
 * @author UMU618 <umu618@hotmail.com>
 * @copyright UMU618 2020
 * @description Use block-always-using-brace npm-coding-style.
 */

const os = require('os')

const conf = require('./conf')

const getIPv6Adresses = () => {
  const addresses = []
  const interfaces = os.networkInterfaces()
  for (const devName in interfaces) {
    const iface = interfaces[devName];
    for (const alias of iface) {
      if (alias.family === 'IPv6' && !alias.internal && alias.scopeid == 0) {
        addresses.push(alias.address)
      }
    }
  }

  return addresses
}

const saveIfChanged = (str) => {
  const fs = require('fs')

  const FN = '/tmp/ipv6-addresses'
  let changed = false

  if (fs.existsSync(FN)) {
    const old = fs.readFileSync(FN, {encoding: 'utf8'})
    if (old != str) {
      changed = true
      fs.writeFileSync(FN, str, {flag: 'w'})
    }
  } else {
    changed = true
    fs.writeFileSync(FN, str, {flag: 'wx'})
  }
  return changed
}

const myIPv6 = getIPv6Adresses()
if (myIPv6) {
  let ips = ''
  myIPv6.sort().forEach(e => { ips += e + '\n' })
  if (saveIfChanged(ips)) {
    setTimeout(() => {
      const alerts = require('./utils/alerts')
      alerts.sendDingtalk(conf.dingtalkInfoToken, conf.dingtalkInfoSecret
        , os.hostname + '\n' + ips)
    }, conf.sleep_sec * 1000) // sleep for network available
  }
}
