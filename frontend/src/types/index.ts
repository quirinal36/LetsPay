export interface Merchant {
  id: string
  email: string
  businessName: string
  businessNumber: string
  representativeName: string
  phone: string
  status: 'PENDING' | 'ACTIVE' | 'SUSPENDED'
}

export interface Customer {
  id: string
  merchantId: string
  name: string
  phone: string
  email?: string
  memo?: string
  tags?: string[]
}

export interface Bill {
  id: string
  merchantId: string
  customerId: string
  billNumber: string
  amount: number
  title: string
  description?: string
  taxType: 'TAX' | 'TAX_FREE'
  sendType: 'IMMEDIATE' | 'SCHEDULED' | 'RECURRING'
  sendChannel: 'ALIMTALK' | 'SMS' | 'BOTH'
  status: 'DRAFT' | 'PENDING' | 'SENT' | 'VIEWED' | 'PAID' | 'CANCELLED' | 'EXPIRED'
  createdAt: string
  updatedAt: string
}
