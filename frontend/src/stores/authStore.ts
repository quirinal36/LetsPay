import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import type { User, Session } from '@supabase/supabase-js'
import { supabase, signIn, signUp, signOut, signInWithGoogle } from '@/lib/supabase'

interface AuthState {
  user: User | null
  session: Session | null
  isLoading: boolean
  error: string | null
  initialize: () => Promise<void>
  login: (email: string, password: string) => Promise<void>
  register: (email: string, password: string) => Promise<void>
  loginWithGoogle: () => Promise<void>
  logout: () => Promise<void>
  clearError: () => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      session: null,
      isLoading: true,
      error: null,

      initialize: async () => {
        try {
          const { data } = await supabase.auth.getSession()
          set({
            session: data.session,
            user: data.session?.user ?? null,
            isLoading: false,
          })
          supabase.auth.onAuthStateChange((_event, session) => {
            set({ session, user: session?.user ?? null })
          })
        } catch {
          set({ isLoading: false, error: 'Failed to initialize auth' })
        }
      },

      login: async (email, password) => {
        set({ isLoading: true, error: null })
        const { data, error } = await signIn(email, password)
        if (error) {
          set({ isLoading: false, error: error.message })
        } else {
          set({ session: data.session, user: data.user, isLoading: false })
        }
      },

      register: async (email, password) => {
        set({ isLoading: true, error: null })
        const { data, error } = await signUp(email, password)
        if (error) {
          set({ isLoading: false, error: error.message })
        } else {
          set({ session: data.session, user: data.user, isLoading: false })
        }
      },

      loginWithGoogle: async () => {
        set({ isLoading: true, error: null })
        const { error } = await signInWithGoogle()
        if (error) {
          set({ isLoading: false, error: error.message })
        }
      },

      logout: async () => {
        set({ isLoading: true })
        await signOut()
        set({ user: null, session: null, isLoading: false })
      },

      clearError: () => set({ error: null }),
    }),
    { name: 'auth-storage', partialize: (state) => ({ user: state.user }) }
  )
)
